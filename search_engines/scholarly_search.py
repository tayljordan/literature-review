import json
import requests
from scholarly import scholarly

def contains_keywords(text, keywords):
    """
    Helper function to check if the text contains any of the keywords.
    The search is case-insensitive.
    """
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords)

def combined_search(query, must_contain=[], max_results=5):
    # Function to search Google Scholar
    def google_scholar_search(query, must_contain, max_results):
        search_query = scholarly.search_pubs(query)
        results = []
        try:
            for _ in range(max_results):
                result = next(search_query)
                title = result.get('bib', {}).get('title', '')
                abstract = result.get('bib', {}).get('abstract', '')

                if contains_keywords(title, must_contain) or contains_keywords(abstract, must_contain):
                    results.append(result)  # Append the result if it contains the required keywords
        except StopIteration:
            pass  # Stop if there are fewer results
        return results

    # Function to search arXiv
    def arxiv_search(query, must_contain, max_results):
        url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            arxiv_data = response.text

            # TODO: Implement XML parsing and keyword matching for arXiv results.
            return arxiv_data
        except requests.RequestException as e:
            return f"Error during arXiv search: {e}"

    # Function to search CrossRef
    def crossref_search(query, must_contain, max_results):
        url = f"https://api.crossref.org/works?query={query}&rows={max_results}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()
            filtered_results = []
            for item in data['message']['items']:
                title = item.get('title', [''])[0]
                abstract = item.get('abstract', '')

                if contains_keywords(title, must_contain) or contains_keywords(abstract, must_contain):
                    filtered_results.append(item)

            return filtered_results
        except requests.RequestException as e:
            return f"Error during CrossRef search: {e}"
        except KeyError:
            return "Invalid response format from CrossRef"

    # Fetch results from different sources
    google_scholar_results = google_scholar_search(query, must_contain, max_results)
    arxiv_results = arxiv_search(query, must_contain, max_results)
    crossref_results = crossref_search(query, must_contain, max_results)

    # Combine results into one dictionary
    combined_results = {
        "Google Scholar Results": google_scholar_results,
        "arXiv Results": arxiv_results,
        "CrossRef Results": crossref_results
    }

    # Convert dictionary to JSON
    return json.dumps(combined_results, indent=4)


