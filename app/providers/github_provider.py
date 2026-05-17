import requests
from app.core.base_provider import BaseProvider

class GitHubProvider(BaseProvider):
    def __init__(self, username):
        # We pass the target username when initializing the provider
        self.username = username
        self._name = "github"

    @property
    def name(self):
        return self._name

    def fetch_data(self):
        """Fetches raw data from the external GitHub API."""
        url = f"https://api.github.com/users/{self.username}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        return None

    def normalize_data(self, raw_data):
        """Converts GitHub's massive JSON response into our clean, unified format."""
        return {
            "username": raw_data.get("login"),
            "profile_url": raw_data.get("html_url"),
            "followers": raw_data.get("followers"),
            "public_repos": raw_data.get("public_repos"),
            "bio": raw_data.get("bio", "No bio available.")
        }