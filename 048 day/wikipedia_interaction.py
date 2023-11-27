from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

wiki_url = "https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Safari()

driver.get(wiki_url)
total_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
in_language = driver.find_element(By.CSS_SELECTOR, value="#articlecount a + a")
print(f"Wiki has {total_articles.text} articles written in {in_language.text} language")

log_in = driver.find_element(By.LINK_TEXT, value="Log in")
# log_in.click()

pre_search = driver.find_element(By.CSS_SELECTOR, value="#p-search > a")
pre_search.click()
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
# alternative way is to click search button
# search_button = driver.find_element(By.CSS_SELECTOR, value="#searchform > button")
# search_button.click()

input("Press enter to quit")
driver.quit()
