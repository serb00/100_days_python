import os
import requests
from tqdm import tqdm

SHEETY_ENDPOINT_FLIGHTDEALS_GET = os.environ.get("SHEETY_ENDPOINT_FLIGHTDEALS_GET")
ENDPOINT_PRICES = SHEETY_ENDPOINT_FLIGHTDEALS_GET + "prices"
ENDPOINT_USERS = SHEETY_ENDPOINT_FLIGHTDEALS_GET + "users"
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
            url=ENDPOINT_PRICES,
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

    def get_cities_without_iata_codes(self) -> list:
        """Get cities without iata codes
        :param self:
        :rtype: list
        """
        return [deal["city"] for deal in self.deals.values() if not deal["is_code"]]

    def fill_iata_codes(self, city_data):
        """Update iata codes
        :param city_data:
        :type city_data: dict
        :param self:
        """
        for city in city_data.keys():
            self.deals[city]["iataCode"] = city_data[city]
            self.deals[city]["is_code"] = True
        self.update_flight_deals(city_data)

    def update_flight_deals(self, cities_to_update):
        """Update flight deals
        :param cities_to_update:
        :param self:
        """
        with tqdm(total=len(cities_to_update), desc="Updating IATA codes for cities", unit="city",
                  ncols=100, colour="green") as pbar:
            for deal in self.deals.values():
                if deal["city"] in cities_to_update.keys():
                    response = requests.put(
                        url=f"{ENDPOINT_PRICES}/{deal['id']}",
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

    @staticmethod
    def get_users():
        """Get users
        :param self:
        :rtype: Response
        """
        response = requests.get(
            url=ENDPOINT_USERS,
            headers=SHEETY_HEADERS,
        )
        response.raise_for_status()
        return response.json()["users"]

    @staticmethod
    def add_user(user):
        """Add user
        :param user:
        :type user: dict
        :param self:
        """
        response = requests.post(
            url=ENDPOINT_USERS,
            json={
                "user": {
                    "firstName": user["firstName"],
                    "lastName": user["lastName"],
                    "fromDestination": user["fromDestination"],
                    "whatsApp": user["whatsApp"],
                }
            },
            headers=SHEETY_HEADERS,
        )
        response.raise_for_status()
