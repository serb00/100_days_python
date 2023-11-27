from selenium import webdriver
from selenium.webdriver.common.by import By
from icecream import ic

url = "https://www.python.org/"
driver = webdriver.Safari()

# url = "https://www.ozon.ru/product/igrovaya-konsol-playstation-5-blu-ray-edition-cfi-1200a-3-reviziya-belyy-603068371/"
# SELECTOR_WITH_CARD = (
#     "#layoutPage > div.b0 > div.container.b4 > div.k5s.kt0 > div.k5s.kt1.sk8.s8k > div.k5s.kt1.sk8.ks9 > "
#     "div.r9l.sl1 > div > div.ls > div > div > div.lp > div.ol6.a2429-a.a2429-a3 > button > span > div > "
#     "div.pj1.p1j > div > div > span")
#
#
# driver.get(url)
# price = driver.find_element(By.CSS_SELECTOR, value=SELECTOR_WITH_CARD)
# print(price.text)


# driver.get(url)

# search_bar = driver.find_element(By.NAME, "q")
# search_bar = driver.find_element(By.ID, "id-search-field")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute("href"))
# bug_link.click()

driver.get(url)

event_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {
    event_id:
        {
            "time": event_date.text,
            "name": event_name.text,
            "link": event_name.get_attribute("href")
        }
    for event_date, event_name, event_id
    in zip(event_dates, event_names, range(len(event_dates)))
}

ic(events)

driver.quit()
