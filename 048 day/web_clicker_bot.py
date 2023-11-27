import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime as dt


PURCHASE_INTERVAL = 3 # seconds
driver = webdriver.Safari()

clicker_url = "https://orteil.dashnet.org/experiments/cookie/"

driver.get(clicker_url)
cookie = driver.find_element(By.ID, value="cookie")


def get_store_items():
    store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    result = []
    try:
        for item in store_items[::-1]:
            if item.get_attribute("class") != "amount":
                item_id = item.get_attribute("id")
                item_price = driver.find_element(By.XPATH, value=f'//*[@id="{item_id}"]/b/text()[2]')
                available = item.get_attribute("class") != "grayed"
                result.append((item, int(item_price.text.replace(",", "")), available))
    except Exception as e:
        print(e)
        print(e.__traceback__)
    return result


def buy_best_store_upgrade(available_money):
    items = get_store_items()
    for upgrade, price, available in items:
        if available and price <= available_money:
            upgrade.click()
            break
        else:
            continue


timer = dt.datetime.now() + datetime.timedelta(seconds=PURCHASE_INTERVAL)
session_end = dt.datetime.now() + datetime.timedelta(minutes=5)
while session_end > dt.datetime.now():
    cookie.click()
    if timer <= dt.datetime.now():
        timer += datetime.timedelta(seconds=PURCHASE_INTERVAL)
        money = driver.find_element(By.ID, value="money")
        current_money = int(money.text.replace(",", ""))
        buy_best_store_upgrade(current_money)

cps = driver.find_element(By.ID, value="cps")
print(cps.text)

driver.quit()
