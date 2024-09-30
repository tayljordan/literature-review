import requests
import time

def search_paper(query):
    search_url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {"query": query}

    for attempt in range(5):
        response = requests.get(search_url, params=params)

        if response.status_code == 200:
            results = response.json()
            return results['data'][0]['paperId'] if results['data'] else None
        elif response.status_code == 429:
            wait_time = 2 ** attempt
            print(f"Error 429: Too Many Requests. Waiting {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print(f"Error: {response.status_code}")
            return None

def get_paper_details(paper_id):
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}"
    params = {"fields": "title,abstract,citations,authors"}

    for attempt in range(5):
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            print("Title:", data.get("title"))
            print("Abstract:", data.get("abstract"))
            print("Authors:", [author['name'] for author in data.get("authors", [])])
            print("Citations:", data.get("citationCount"))
            return
        elif response.status_code == 429:
            wait_time = 2 ** attempt
            print(f"Error 429: Too Many Requests. Waiting {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print(f"Error: {response.status_code}")
            return

search_query = "Title of the Paper/ Eg: Crack identification for marine engineering equipment based on improved SSD and YOLOv5"
paper_id = search_paper(search_query)

if paper_id:
    get_paper_details(paper_id)
