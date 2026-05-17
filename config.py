import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# We store everything in a dictionary to easily pass to the PUAPIEngine
Config = {
    "GITHUB_USERNAME": os.getenv("GITHUB_USERNAME"),
    "COINGECKO_COINS": os.getenv("COINGECKO_COINS"),  # This is a comma-separated string of coin IDs for the CoinGecko module
    "OPENWEATHER_API_KEY": os.getenv("OPENWEATHER_API_KEY"),
    "WEATHER_CITY": os.getenv("WEATHER_CITY", "London"), # Defaults to London if empty
    "NEWS_API_KEY": os.getenv("NEWS_API_KEY"),
    "NEWS_CATEGORY": os.getenv("NEWS_CATEGORY", "technology"),
    "TMDB_API_KEY": os.getenv("TMDB_API_KEY")
    # Future keys will go here:
    # "WEATHER_API_KEY": os.getenv("WEATHER_API_KEY")
}