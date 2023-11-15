import requests
import datetime
import os
from twilio.rest import Client

# ------- Constants and variables block ------- #
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCKS_API_KEY = os.environ.get("STOCKS_API_KEY")
TWILIO_SID = os.environ.get("TW_A_SID")
TWILIO_TOKEN = os.environ.get("TW_TOKEN")

STOCK = "TSLA"
STOCK_URL = "https://www.alphavantage.co/query"
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCKS_API_KEY
}

COMPANY_NAME = "Tesla Inc"
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_PARAMETERS = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}


# --------------------- Functions block --------------------- #
def get_stock_price_difference() -> float:
    """Returns the difference between yesterday's and the
    day before yesterday's closing price in percents"""
    response = requests.get(STOCK_URL, params=STOCK_PARAMETERS)
    response.raise_for_status()

    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    day_before = today - datetime.timedelta(days=2)
    yesterday_data = response.json()["Time Series (Daily)"][str(yesterday)]
    day_before_data = response.json()["Time Series (Daily)"][str(day_before)]
    yesterday_closing_price = float(yesterday_data["4. close"])
    day_before_closing_price = float(day_before_data["4. close"])

    return abs((yesterday_closing_price - day_before_closing_price) / day_before_closing_price * 100)


def get_company_news() -> list:
    """Returns the first 3 news pieces for the company"""
    response = requests.get(NEWS_URL, params=NEWS_PARAMETERS)
    response.raise_for_status()

    return response.json()["articles"][0:3]


def send_message(body):
    """Sends a message to the phone number by WhatsApp"""
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    message = client.messages.create(
        body=body,
        from_="whatsapp:+14155238886",
        to="whatsapp:+79957873534"
    )
    print(f"message status: {message.status}.")


def format_message(difference, news):
    if difference > 0:
        emoji = "🔺"
    else:
        emoji = "🔻"

    return f"{STOCK}: {emoji}{difference :.2f}%\n\n" \
           f"Headline: {news[0]['title']}\n" \
           f"Brief: {news[0]['description']}\n\n" \
           f"Headline: {news[1]['title']}\n" \
           f"Brief: {news[1]['description']}\n\n" \
           f"Headline: {news[2]['title']}\n" \
           f"Brief: {news[2]['description']}"


# --------------------- Main program --------------------- #
if __name__ == '__main__':
    diff = get_stock_price_difference()
    if diff > 4:
        send_message(format_message(diff, get_company_news()))
