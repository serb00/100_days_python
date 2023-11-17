import datetime as dt

from tqdm import tqdm

from locations import Locations
from excell import FlightDeals
from flights_search import FlightsSearch
from notifications import NotificationManager


FROM_CITY = "LON"
FROM_DATE = (dt.date.today() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
TO_DATE = (dt.date.today() + dt.timedelta(days=90)).strftime("%d/%m/%Y")

if __name__ == "__main__":
    print("Welcome to Flight Club.")
    print("We find the best flight deals and email you.")
    fd = FlightDeals()
    if not fd.all_have_iata_codes():
        locations = Locations(fd.deals.keys())
        fd.fill_iata_codes(locations.cities)
        print("IATA codes updated.")
    fs = FlightsSearch()
    best_flights = {}
    with tqdm(total=len(fd.deals), desc="Searching for best flight prices", unit="city",
              ncols=100, colour="green") as pbar:
        for deal in fd.deals.values():
            flights = fs.get_flights(
                from_city=FROM_CITY,
                to_city=deal["iataCode"],
                from_date=FROM_DATE,
                to_date=TO_DATE,
            )
            best_deal_found = False
            for flight in flights:
                best_price = deal["price"]
                if flight["price"] <= best_price:
                    best_deal_found = True
                    best_flights[deal["city"]] = flight

            pbar.update(1)

    if best_flights:
        print("Best flights found. Sending details to your whatsapp.")
        for city, flight in best_flights.items():
            nm = NotificationManager()
            message = nm.format_message(flight)
            status = nm.send_whatsapp_message(message)
            print(f"message status: {status}.")
    else:
        print("No flights found, try another time.")
