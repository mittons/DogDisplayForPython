import requests
import re

class DogBreedService:
    def __init__(self, base_url):
        self.base_url = base_url
        self.allowed_chars = re.compile(r"[a-zA-Z0-9\(\)\-\,\.\!]")

    # Fetches data from the external service defined by the base_url variable.
    #
    # Should return a dictionary of data, or None if that is not possible (e.g. on errors, etc.)
    def get_data(self):
        response = None
        try:
            response = requests.get(f"{self.base_url}/breeds")
            response.raise_for_status()
        except requests.RequestException:
            return None
        
        if (response.status_code != 200):
            return None
        
        data = response.json()
        return self._sanitize_data(data)

    # Filters out any variables we are not using.
    # - For the variables we are using it removes any character we have not whitelisted (see _sanitize_string function for details).
    def _sanitize_data(self, data):
        sanitized_data = []
        for item in data:
            name = self._sanitize_string(item.get('name', ''))
            temperament = self._sanitize_string(item.get('temperament', ''))
            sanitized_data.append({'name': name, 'temperament': temperament})
        return sanitized_data

    def _sanitize_string(self, string):
        # Replace or remove unsafe characters
        return re.sub(r"[^a-zA-Z0-9\(\)\-\,\.\!\ ]", "", string)
