import requests
from twilio.rest import Client
from twilio.rest.api.v2010.account.message import MessageInstance
import os

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TW_A_SID")
auth_token = os.environ.get("TW_TOKEN")
MY_WHATSAPP = os.environ.get("MY_WHATSAPP")
weather_url = "http://api.openweathermap.org/data/2.5/forecast"
location_url = "http://api.openweathermap.org/geo/1.0/direct"


def will_rain(weather_data):
    for weather_3_hours in weather_data:
        for weather in weather_3_hours["weather"]:
            if int(weather["id"]) < 700:
                return True

    return False


def send_whats_app_message(rainy) -> MessageInstance:
    """Sends a message to the phone number by WhatsApp"""
    client = Client(account_sid, auth_token)

    if rainy:
        body = "It's gonna rain"
    else:
        body = "No rain for next 12 hours"

    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=body,
        to=f"whatsapp:{MY_WHATSAPP}"
    )

    return message


city = input("Provide the city name: ")

parameters_location = {
    "q": city,
    "limit": 5,
    "appid": api_key,
}

response = requests.get(url=location_url, params=parameters_location)
response.raise_for_status()
lat = float(response.json()[0]["lat"])
lon = float(response.json()[0]["lon"])
print(f"city: {city}\nlat: {lat}\nlon: {lon}")

parameters_weather = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
}

response = requests.get(url=weather_url, params=parameters_weather)
response.raise_for_status()
weather_next_12_hours = response.json()["list"][0:4]

msg = send_whats_app_message(will_rain(weather_next_12_hours))
# print(msg.status)
