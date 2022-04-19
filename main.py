from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up Selenium
chrome_driver_path = "C:\Development\chromedriver.exe"
s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Locating the cookie
cookie = driver.find_element(by=By.ID, value="cookie")

# Establishing time to exit (t_exit) and time to check (t_end)
t_exit = time.time() + 5 *60
t_end = time.time() + 5

# Setting up a list of IDs of things you can buy at the store. We need the IDs and not the class names for later code
# We can instruct a click using the ID names and not the class names
store = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
items = [item.get_attribute("ID") for item in store]

while time.time() < t_exit:
    #Clicking the cookie!
    while time.time() < t_end:
        cookie.click()

    # Check how much money I have
    money = int(driver.find_element(by=By.ID, value="money").text.replace(",", ""))

    # Finding the prices of each upgrade
    menu = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")

    # Putting the prices as integers in a list, manually adding in a dummy price for Elder's Pledge (Quirk in the game)
    prices = []
    for price in menu:
        if price.text != "":
            cost = int(price.text.split("-")[1].strip().replace(",", ""))
            prices.append(cost)
        else:
            prices.append(666666)

    # Making a dictionary out of the ID list and prices list
    upgrades = {}
    for i in range(len(items)):
        upgrades[items[i]] = prices[i]

    # Making a dictionary out of the upgrades I can afford
    affordable_upgrades = {key: values for (key, values) in upgrades.items() if money > values}

    # Making a dictionary out of the upgrades I can afford
    if affordable_upgrades:
        dearest_upgrade = max(affordable_upgrades, key=affordable_upgrades.get)
        driver.find_element(by=By.ID, value=dearest_upgrade).click()

    # Resetting things for the next loop

    prices.clear()
    upgrades.clear()
    affordable_upgrades.clear()
    t_end = time.time() + 5

# When five minutes have passed, work out the cookies/second rate

cps = driver.find_element(by=By.ID, value="cps").text

print(f"Your final {cps}.")