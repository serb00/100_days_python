import requests
from datetime import datetime
# from geopy.geocoders import Nominatim
import geocoder


def get_lat_long_by_city():
    # geolocator = Nominatim(user_agent="iss overhead checker")
    # city_name = input("City Name Here:")
    # location = geolocator.geocode(city_name)
    # return location.latitude, location.longitude

    city_name = input("City Name Here:")
    g = geocoder.osm(city_name)
    if g.ok:
        return g.lat, g.lng
    else:
        print("Geocoding failed, sending Johor Bahru coordinates.")
        return 1.492659, 103.741356


def is_iss_above_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if ((my_lat - 5 < iss_latitude < my_lat + 5) &
            (my_long - 5 < iss_longitude < my_long + 5)):
        return True
    else:
        print(iss_latitude)
        print(iss_longitude)
        return False


def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_zone = datetime.now().astimezone().tzinfo.__str__()
    if time_zone[0] == "+":
        _, sunrise = divmod(sunrise + int(time_zone[1:]), 24)
        _, sunset = divmod(sunset + int(time_zone[1:]), 24)
    elif time_zone[0] == "-":
        _, sunrise = divmod(sunrise - int(time_zone[1:]), 24)
        _, sunset = divmod(sunset - int(time_zone[1:]), 24)
    else:
        print("Something wrong with time zone detection")

    time_now = datetime.now().hour

    if time_now > sunset or time_now < sunrise:
        return True
    else:
        return False


my_lat, my_long = get_lat_long_by_city()

parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0,
}


if is_iss_above_me() & is_dark():
    print("It's here")
elif not is_dark():
    print("It's day time")
else:
    print("It's far")

