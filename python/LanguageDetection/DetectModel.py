import requests
from iso639 import languages

class DetectModel:
    def __init__(self, api_url="http://127.0.0.1:5000/lg"):
        self.api_url = api_url

    def detect_language(self, text):
        try:
            response = requests.get(self.api_url, params={'id': text})
            response.raise_for_status()  # Fehler werfen, falls der Status nicht OK ist
            print(response.text)
            data = response.json()
            print(data)
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error in request: {e}")
            return None

    def get_language_name(self, short_code):
        try:
            print("try get_language erreicht")
            print(short_code)
            #lang = iso639.get_name(short_code)
            lang = languages.get(alpha2=short_code)
            print(lang.name)
            return lang.name
        except KeyError:
            return "Unknown language"