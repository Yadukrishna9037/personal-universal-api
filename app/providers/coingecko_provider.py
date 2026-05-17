import requests
from app.core.base_provider import BaseProvider

class CoinGeckoProvider(BaseProvider):
    def __init__(self, coins):
        # We pass the list of coins (e.g., "bitcoin,ethereum") from our config
        self.coins = coins
        self._name = "crypto_prices"

    @property
    def name(self):
        return self._name

    def fetch_data(self):
        """Calls the free CoinGecko simple price API."""
        # vs_currencies=usd means we want the price in US Dollars
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={self.coins}&vs_currencies=usd"
        
        # Adding a basic header as CoinGecko sometimes blocks default Python user-agents
        headers = {
            "accept": "application/json",
            "User-Agent": "PU-API-Client"
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        return None

    def normalize_data(self, raw_data):
        """
        CoinGecko returns data like: {"bitcoin": {"usd": 65000}, "ethereum": {"usd": 3500}}
        We will clean it up slightly to ensure a consistent output format.
        """
        normalized = []
        for coin, price_data in raw_data.items():
            normalized.append({
                "coin": coin.capitalize(),
                "price_usd": price_data.get("usd")
            })
            
        return normalized