from abc import ABC, abstractmethod

class BaseProvider(ABC):
    """
    Abstract base class for all external service providers.
    Every new module (GitHub, Weather, Spotify, etc.) MUST inherit from this 
    and implement these specific methods.
    """

    @property
    @abstractmethod
    def name(self):
        """Returns the unique string name of the provider (e.g., 'github')."""
        pass

    @abstractmethod
    def fetch_data(self):
        """Logic to call the external API and get the raw JSON response."""
        pass

    @abstractmethod
    def normalize_data(self, raw_data):
        """Logic to convert the messy external JSON into our clean PU-API format."""
        pass

    def get_data(self):
        """
        The main method called by the API engine. 
        It orchestrates fetching and formatting automatically.
        """
        try:
            raw_data = self.fetch_data()
            if not raw_data:
                return {"error": "No data returned from external API."}
            return self.normalize_data(raw_data)
        except Exception as e:
            return {"error": f"Provider '{self.name}' failed: {str(e)}"}