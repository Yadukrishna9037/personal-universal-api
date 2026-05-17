import requests
from app.core.base_provider import BaseProvider

class WeatherProvider(BaseProvider):
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city
        self._name = "weather"

    @property
    def name(self):
        return self._name

    def fetch_data(self):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    def normalize_data(self, raw_data):
        return {
            "city": raw_data.get("name"),
            "temperature_celsius": raw_data["main"].get("temp"),
            "description": raw_data["weather"][0].get("description").capitalize() if raw_data.get("weather") else "Unknown",
            "humidity": raw_data["main"].get("humidity")
        }