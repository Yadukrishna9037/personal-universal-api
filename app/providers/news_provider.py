import requests
from app.core.base_provider import BaseProvider

class NewsProvider(BaseProvider):
    def __init__(self, api_key, category):
        self.api_key = api_key
        self.category = category
        self._name = "top_news"

    @property
    def name(self):
        return self._name

    def fetch_data(self):
        url = f"https://newsapi.org/v2/top-headlines?category={self.category}&language=en&apiKey={self.api_key}"
        headers = {"User-Agent": "PU-API-Client"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None

    def normalize_data(self, raw_data):
        # Grab only the top 3 articles to keep the payload clean
        articles = raw_data.get("articles", [])[:3]
        
        normalized = []
        for a in articles:
            normalized.append({
                "title": a.get("title"),
                "source": a.get("source", {}).get("name"),
                "url": a.get("url")
            })
        return normalized