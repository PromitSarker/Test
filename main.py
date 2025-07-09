from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.bing.com")

input_element = driver.find_element(By.CLASS_NAME, "sb_form_q")
input_element.send_keys("Hexagons")
#Submitting the form directly cz keys.enter faces some issues in some cases
# input_element.send_keys(Keys.ENTER)
input_element.submit()


time.sleep(10)
driver.quit()
