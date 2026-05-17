import requests
from app.core.base_provider import BaseProvider

class TMDBProvider(BaseProvider):
    def __init__(self, api_key):
        self.api_key = api_key
        self._name = "trending_movies"

    @property
    def name(self):
        return self._name

    def fetch_data(self):
        url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    def normalize_data(self, raw_data):
        # Grab only the top 3 trending movies
        movies = raw_data.get("results", [])[:3]
        
        normalized = []
        for m in movies:
            normalized.append({
                "title": m.get("title"),
                "rating": m.get("vote_average"),
                "release_date": m.get("release_date")
            })
        return normalized