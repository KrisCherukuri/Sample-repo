import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Users/Kishore/chromedriver_win32/chromedriver.exe")
driver.set_page_load_timeout("10")

driver.delete_all_cookies()
driver.get("https://wa.me/919988776655?text=How%20are%20you%20?")
driver.find_element_by_id("action-button").send_keys(Keys.ENTER)