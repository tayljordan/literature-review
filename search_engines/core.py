import requests

# Define the base URL and headers for the request
base_url = "https://api.core.ac.uk/v3/search/works"
query = "examining marine engineering drawings using python imaging tool"  # Define the query for the search
keyword = "maritime"  # Keyword to refine the search to maritime-related results
query_params = {
    'q': query,  # Your search query
    'limit': 5,  # Limit to 5 results for more context
    'keyword': keyword  # Filter by the keyword 'maritime'
}
headers = {
    'Accept': 'application/json'  # Ensure we get a JSON response
}

# Send the GET request to the API
try:
    response = requests.get(base_url, params=query_params, headers=headers)

    # Raise an HTTP error for bad responses (4xx, 5xx)
    response.raise_for_status()

    # Parse the JSON data from the response
    results = response.json()

    # Check if we got results and print them
    if results:
        print(f"Search Results related to '{keyword}':")
        for result in results.get('results', []):
            print(f"Title: {result.get('title')}")
            print(f"Authors: {', '.join(author['name'] for author in result.get('authors', []))}")
            print(f"Published: {result.get('publishedYear')}")
            print(f"DOI: {result.get('doi', 'N/A')}")
            print(f"URL: {result.get('url')}")
            # Print abstract if available
            abstract = result.get('abstract', 'Abstract not available')
            print(f"Abstract: {abstract[:300]}...")  # Print a snippet of the abstract
            print("-" * 40)
    else:
        print("No results found for your query.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
except Exception as err:
    print(f"An error occurred: {err}")  # Handle other exceptions
