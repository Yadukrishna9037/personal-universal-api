import time
from app.providers.github_provider import GitHubProvider
from app.providers.coingecko_provider import CoinGeckoProvider
from app.providers.weather_provider import WeatherProvider     # <-- New
from app.providers.news_provider import NewsProvider           # <-- New
from app.providers.movie_provider import TMDBProvider

class PUAPIEngine:
    def __init__(self, config):
        self.providers = []
        self._register_providers(config)
        
        # --- NEW CACHING VARIABLES ---
        self.cached_data = None
        self.last_fetched = 0
        self.cache_duration = 300 # Cache timeout in seconds (5 minutes)

    def _register_providers(self, config):
        if config.get("GITHUB_USERNAME"):
            self.providers.append(
                GitHubProvider(username=config.get("GITHUB_USERNAME"))
            )
        if config.get("COINGECKO_COINS"):
            self.providers.append(
                CoinGeckoProvider(coins=config.get("COINGECKO_COINS"))
            )
        if config.get("OPENWEATHER_API_KEY"):
            self.providers.append(WeatherProvider(
                api_key=config.get("OPENWEATHER_API_KEY"),
                city=config.get("WEATHER_CITY")
            ))
            
        if config.get("NEWS_API_KEY"):
            self.providers.append(NewsProvider(
                api_key=config.get("NEWS_API_KEY"),
                category=config.get("NEWS_CATEGORY")
            ))
            
        if config.get("TMDB_API_KEY"):
            self.providers.append(TMDBProvider(api_key=config.get("TMDB_API_KEY")))
            
    def get_all_data(self):
        # Check if we have cached data AND if it's less than 5 minutes old
        current_time = time.time()
        if self.cached_data and (current_time - self.last_fetched < self.cache_duration):
            print("Serving from Cache!") # This will print in your terminal so you can see it working
            return self.cached_data

        print("Fetching fresh data from APIs...")
        aggregated_data = {}
        
        for provider in self.providers:
            aggregated_data[provider.name] = provider.get_data()
            
        # Format the response
        response = {
            "status": "success",
            "data": aggregated_data
        }
        
        # Save the new response to our cache and update the timestamp
        self.cached_data = response
        self.last_fetched = current_time
        
        return response