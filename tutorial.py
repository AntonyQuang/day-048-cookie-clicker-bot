from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
s = Service(chrome_driver_path)
#
# driver = webdriver.Chrome(service=s)
#
# driver.get("https://www.amazon.co.uk/Logitech-Wireless-Keyboard-Windows-Connection/dp/B00CL6353A")
# price = driver.find_element(by=By.CLASS_NAME, value="a-offscreen")
# print(price)
# print(price.text)
#
# driver.close()

driver = webdriver.Chrome(service=s)
driver.get("https://www.python.org/")

# search_bar = driver.find_element(by=By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
#
# documentation_link = driver.find_element(by=By.CSS_SELECTOR, value=".docs-meta a")
# print(documentation_link.get_attribute("href"))
#
# website_bug_link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(website_bug_link.text)

times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget .menu time")
names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget .menu a")
# print(times[0].get_attribute("datetime").split("T")[0])
# print(names[0].text)

events = {i: {"time": times[i].get_attribute("datetime").split("T")[0],
              "name": names[i].text}
          for i in range(len(times))}
print(events)

driver.close()