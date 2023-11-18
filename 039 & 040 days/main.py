import datetime as dt

from tqdm import tqdm

from locations import Locations
from excell import FlightDeals
from flights_search import FlightsSearch
from notifications import NotificationManager

FROM_DATE = (dt.date.today() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
TO_DATE = (dt.date.today() + dt.timedelta(days=90)).strftime("%d/%m/%Y")


def find_best_price(list_flights, deal):
    tmp_best_prices = {}
    for flight in list_flights:
        best_price = deal["price"]
        if flight["price"] <= best_price:
            tmp_best_prices[deal["city"]] = flight
    return tmp_best_prices


def find_best_flights(deals, from_city_name):
    fs = FlightsSearch()
    tmp_best_flights = {}
    from_city = Locations.get_iata_code(from_city_name)
    with tqdm(total=len(deals), desc="Searching for best flight prices", unit="city",
              ncols=100, colour="green") as pbar:
        for deal in deals.values():
            flights = fs.get_flights(
                from_city=from_city,
                to_city=deal["iataCode"],
                from_date=FROM_DATE,
                to_date=TO_DATE,
            )

            for name, price in find_best_price(flights, deal).items():
                tmp_best_flights[name] = price

            pbar.update(1)

    return tmp_best_flights


def verify_iata_codes(flight_deals):
    if not flight_deals.all_have_iata_codes():
        print("Some cities don't have IATA codes. Updating...")
        locations = Locations(flight_deals.get_cities_without_iata_codes())
        flight_deals.fill_iata_codes(locations.cities)
        print("IATA codes updated.")


def notify_user(best_flights_found, user_to_notify):
    if best_flights_found:
        print("Best flights found. Sending details to your whatsapp.")
        for city, flight in best_flights_found.items():
            nm = NotificationManager()
            message = nm.format_message(flight)
            status = nm.send_whatsapp_message(user_to_notify, message)
            print(f"message status: {status}.")
    else:
        print("No flights found, try another time.")


def register_user():
    global user
    # Ask for user parameters input
    user_first_name = input("What is your name? ")
    user_last_name = input("What is your last name? ")
    user_from_destination = input("From where you want to depart? ")
    user_whatsapp = input("What is your whatsapp number? ")
    user = {
        "firstName": user_first_name,
        "lastName": user_last_name,
        "fromDestination": user_from_destination,
        "whatsApp": user_whatsapp
    }
    fd.add_user(user)
    print("User added. You will receive a message when we find the best flight deals.")


if __name__ == "__main__":
    print("Welcome to Flight Club.")
    print("We find the best flight deals and inform you.")
    fd = FlightDeals()
    answer = input("Do you want to Register or Check your flight deals? ")

    if answer.lower() == "register" or answer.lower() == "r":
        register_user()
    elif answer.lower() == "check" or answer.lower() == "c":
        verify_iata_codes(fd)
        users = fd.get_users()
        for user in users:
            print(f"Searching for best flights for {user['firstName']} {user['lastName']}.")
            best_flights = find_best_flights(fd.deals, user["fromDestination"])
            notify_user(best_flights, user)
