import requests

api_url = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "category": 9,
    "type": "boolean"
}

response = requests.get(api_url, params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
