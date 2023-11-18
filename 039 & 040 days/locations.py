import os
import requests
from tqdm import tqdm

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")

TEQUILA_LOCATIONS_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_HEADERS = {
    "accept": "application/json",
    "apikey": TEQUILA_API_KEY,
}


class Locations:
    def __init__(self, list_of_cities):
        self.cities = {city: "" for city in list_of_cities}
        self.get_iata_codes()

    def get_iata_codes(self):
        with tqdm(total=len(self.cities), desc="Getting IATA codes for cities", unit="city",
                  ncols=100, colour="green") as pbar:
            for city in self.cities.keys():
                self.cities[city] = self.get_iata_code(city)

                pbar.update(1)

    @staticmethod
    def get_iata_code(city):
        parameters = {
            "term": city,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 1,
            "active_only": "true",
            "sort": "name",
        }
        response = requests.get(
            url=TEQUILA_LOCATIONS_ENDPOINT,
            headers=TEQUILA_HEADERS,
            params=parameters,
        )
        response.raise_for_status()
        data = response.json()
        return data["locations"][0]["code"]
