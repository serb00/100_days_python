import os
import requests


class FlightsSearch:
    def __init__(self):
        self.tequila_api_key = os.environ.get("TEQUILA_API_KEY")
        self.tequila_flights_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.tequila_headers = {
            "apikey": self.tequila_api_key,
            "accept": "application/json",
        }

    def get_flights(self, from_city, to_city, from_date, to_date):
        tequila_parameters = {
            "fly_from": "city:" + from_city,
            "fly_to": "city:" + to_city,
            "date_from": from_date,
            "date_to": to_date,
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "14",
            "ret_from_diff_city": "false",
            "ret_to_diff_city": "false",
            "one_for_city": "1",
            "one_per_date": "1",
            "adults": "2",
            "selected_cabins": "M",
            "adult_hold_bag": "1,1",
            "adult_hand_bag": "1,1",
            "only_working_days": "false",
            "only_weekends": "false",
            "partner_market": "tr",
            "curr": "EUR",
            "locale": "en",
            "max_stopovers": "2",
            "max_sector_stopovers": "2",
            "vehicle_type": "aircraft",
            "limit": "100",
        }
        response = requests.get(
            url=self.tequila_flights_endpoint,
            headers=self.tequila_headers,
            params=tequila_parameters,
        )
        response.raise_for_status()
        return response.json()["data"]
