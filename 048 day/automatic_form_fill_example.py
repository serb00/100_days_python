from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

form_url = "http://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Safari()

driver.get(form_url)
name_field = driver.find_element(By.NAME, value="fName")
name_field.send_keys("John")
time.sleep(1)
last_name_field = driver.find_element(By.NAME, value="lName")
last_name_field.send_keys("Doe")
time.sleep(1)
email_field = driver.find_element(By.NAME, value="email")
email_field.send_keys("test@test.com")
time.sleep(1)
email_field.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
