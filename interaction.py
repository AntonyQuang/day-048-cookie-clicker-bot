from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
#
#
# all_portals = driver.find_element(by=By.LINK_TEXT, value="Current events")
# all_portals.click()
#
#
# search_bar = driver.find_element(by=By.NAME, value="search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(by=By.NAME, value="fName")
last_name = driver.find_element(by=By.NAME, value="lName")
email = driver.find_element(by=By.NAME, value="email")
sign_up_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

first_name.send_keys("Jonathan")
last_name.send_keys("Ronathan")
email.send_keys("JR@email.com")
sign_up_button.click()