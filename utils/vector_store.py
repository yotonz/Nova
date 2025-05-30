# utils/vector_store.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX")

def search_documents(query: str, top_k: int = 5):
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_SEARCH_KEY
    }
    payload = {
        "search": query,
        "top": top_k
    }

    search_url = f"{AZURE_SEARCH_ENDPOINT}/indexes/{AZURE_SEARCH_INDEX}/docs/search?api-version=2023-07-01"
    response = requests.post(search_url, headers=headers, json=payload)

    if response.status_code == 200:
        results = response.json().get("value", [])
        return [doc.get("content", "") for doc in results if "content" in doc]
    else:
        print("Search error:", response.text)
        return []
