import requests
from django.conf import settings



def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        
    }
    response = requests.get(url, params=params)
    return response.json()
