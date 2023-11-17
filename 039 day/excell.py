import os
import requests
from tqdm import tqdm

SHEETY_ENDPOINT_FLIGHTDEALS_GET = os.environ.get("SHEETY_ENDPOINT_FLIGHTDEALS_GET")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_HEADERS = {
    "Authorization": "Bearer " + SHEETY_TOKEN,
}


class FlightDeals:
    def __init__(self):
        self.deals = {}
        self.get_flight_deals()

    def get_flight_deals(self):
        """Get flight deals from Google sheet via sheety
        :param self:
        :rtype: Response
        """
        tmp_deals = {}
        response = requests.get(
            url=SHEETY_ENDPOINT_FLIGHTDEALS_GET,
            headers=SHEETY_HEADERS,
        )
        response.raise_for_status()
        for deal in response.json()["prices"]:
            tmp_deals[deal["city"]] = {"iataCode": deal["iataCode"],
                                       "city": deal["city"],
                                       "price": deal["lowestPrice"],
                                       "is_code": deal["iataCode"] != "",
                                       "id": deal["id"]}
        self.deals = tmp_deals

    def all_have_iata_codes(self) -> bool:
        """Check if all cities have iata codes
        :param self:
        :rtype: bool
        """
        return all([deal["is_code"] for deal in self.deals.values()])

    def fill_iata_codes(self, city_data):
        """Update iata codes
        :param city_data:
        :type city_data: dict
        :param self:
        """
        for city in city_data.keys():
            self.deals[city]["iataCode"] = city_data[city]
            self.deals[city]["is_code"] = True
        self.update_flight_deals()

    def update_flight_deals(self):
        """Update flight deals
        :param self:
        """
        with tqdm(total=len(self.deals), desc="Updating IATA codes for cities", unit="city",
                  ncols=100, colour="green") as pbar:
            for deal in self.deals.values():
                response = requests.put(
                    url=f"{SHEETY_ENDPOINT_FLIGHTDEALS_GET}/{deal['id']}",
                    json={
                        "price": {
                            "city": deal["city"],
                            "iataCode": deal["iataCode"],
                            "lowestPrice": deal["price"],
                        }
                    },
                    headers=SHEETY_HEADERS,
                )
                response.raise_for_status()

                pbar.update(1)
