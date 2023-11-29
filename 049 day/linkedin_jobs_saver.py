from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

MY_LINKEDIN_LOGIN = os.environ.get("MY_LINKEDIN_LOGIN")
MY_LINKEDIN_PASS = os.environ.get("MY_LINKEDIN_PASS")

driver = webdriver.Safari()

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3712315398&f_AL=true&f_E=2&f_T=25169&f_WT=2&geoId=92000000&keywords=Python%20developer&location=Worldwide&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD#HYM")

time.sleep(2)
accept_cookies = driver.find_element(
    By.CSS_SELECTOR, value="#artdeco-global-alert-container > div > section > div > div.artdeco-global-alert-action__wrapper > button:nth-child(1)")
accept_cookies.click()
time.sleep(1)
sign_in = driver.find_element(By.PARTIAL_LINK_TEXT, value="Sign in")
sign_in.click()
time.sleep(2)
username = driver.find_element(By.ID, value="username")
username.send_keys(MY_LINKEDIN_LOGIN)
password = driver.find_element(By.ID, value="password")
password.send_keys(MY_LINKEDIN_PASS)
time.sleep(1)
password.send_keys(Keys.ENTER)
time.sleep(10)

list_of_jobs = driver.find_elements(
    By.CSS_SELECTOR, value=".job-card-list__title")

print(f"found {len(list_of_jobs)} jobs")

for job in list_of_jobs:
    print(job.text)
    job.send_keys(Keys.SHIFT)
    job.click()
    time.sleep(2)
    try:
        save = driver.find_element(
            By.CSS_SELECTOR, value=".jobs-save-button")
        save.send_keys(Keys.SHIFT)
        save.click()
        time.sleep(2)
    except ValueError:
        print("error finding save button")
        continue

input("Press enter to continue")

driver.quit()
