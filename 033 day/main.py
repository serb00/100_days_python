import requests
from icecream import ic
import datetime

# response = requests.request("GET", "http://api.open-notify.org/iss-now.json")
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

result = response.json()["iss_position"]
print(f'https://www.latlong.net/c/?lat={result["latitude"]}&long={result["longitude"]}')

parameters = {
    "lat": result['latitude'],
    "lng": result['longitude'],
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
result = response.json()["results"]
ic(result["sunset"])
