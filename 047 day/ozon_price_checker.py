import pyshorteners
from bs4 import BeautifulSoup
from zenrows import ZenRowsClient
import os

from notifications import NotificationManager

ZENROWS_API_KEY = os.environ.get("ZENROWS_API_KEY")
MY_WHATSAPP = os.environ.get("MY_WHATSAPP")
SELECTOR_WITH_CARD = (
    "#layoutPage > div.b0 > div.container.b4 > div.k5s.kt0 > div.k5s.kt1.sk8.s8k > div.k5s.kt1.sk8.ks9 > "
    "div.r9l.sl1 > div > div.ls > div > div > div.lp > div.ol6.a2429-a.a2429-a3 > button > span > div > "
    "div.pj1.p1j > div > div > span")
SELECTOR_WITH_CARD_ALT = (
    "#layoutPage > div.b0 > div.container.b4 > div.k5s.kt0 > div.k5s.kt1.sk8.s8k > div.k5s.kt1.sk8.ks9 > div > div > "
    "div.ls > div > div > div.lp > div.ol6.a2429-a.a2429-a3 > button > span > div > div.pj1.p1j > div > div > span")

SELECTOR_WITHOUT_CARD = (
    "#layoutPage > div.b0 > div.container.b4 > div.k5s.kt0 > div.k5s.kt1.sk8.s8k > div.k5s.kt1.sk8.ks9 > div > div > "
    "div.ls > div > div > div.lp > div.pl2.pl7 > div > div.p5l > span.p3l.lp4.p7l")
SELECTOR_WITHOUT_CARD_ALT = (
    "#layoutPage > div.b0 > div.container.b4 > div.k5s.kt0 > div.k5s.kt1.sk8.s8k > div.k5s.kt1.sk8.ks9 > div > div > "
    "div.ls > div > div > div.lp > div.pl2.pl7 > div > div.p5l > span.p3l.lp4.p7l")

SELECTOR_TITLE = "#layoutPage > div.b0 > div.container.b4 > div:nth-child(2) > div > div > div.k5s.kt1.sk9 > div > h1ß"
SELECTOR_TITLE_ALT = ("#layoutPage > div.b0 > div.container.b4 > div:nth-child(2) > div > div > div.k5s.kt1.sk9 > div "
                      "> h1")

client = ZenRowsClient(ZENROWS_API_KEY)
url = "https://www.ozon.ru/product/igrovaya-konsol-playstation-5-blu-ray-edition-cfi-1200a-3-reviziya-belyy-603068371/"
params = {"js_render": "true",
          "premium_proxy": "true"}


if __name__ == '__main__':
    print("Welcome to the Ozon price checker!")
    user_url = input('Please enter a URL for product or leave empty for default url: ')
    if user_url:
        url = user_url
    response = client.get(url, params=params)

    soup = BeautifulSoup(response.text, "html.parser")
    try:
        price_text = soup.select_one(SELECTOR_WITH_CARD).getText()
        price_without_card_text = soup.select_one(SELECTOR_WITHOUT_CARD).getText()
        title = soup.select_one(SELECTOR_TITLE).getText()
    except AttributeError:
        price_text = soup.select_one(SELECTOR_WITH_CARD_ALT).getText()
        price_without_card_text = soup.select_one(SELECTOR_WITHOUT_CARD_ALT).getText()
        title = soup.select_one(SELECTOR_TITLE_ALT).getText()

    # price text example "56 255 ₽"
    result = int(price_text.replace(" ", "").replace("₽", ""))
    result_without_card = int(price_without_card_text.replace(" ", "").replace("₽", ""))

    nm = NotificationManager()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    message = (f"\n{title}:\n"
               f"Купить по ссылке: {short_url}\n"
               f"Цена с картой OZON: {result} ₽\n"
               f"Цена без карты OZON: {result_without_card} ₽")
    nm.send_whatsapp_message({"whatsApp": MY_WHATSAPP}, message)
    print(message)
