import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# create a new Firefox session
driver = webdriver.Firefox()

driver.maximize_window()

# navigate to the application home page
driver.get("https://www.saucedemo.com/")

driver.implicitly_wait(30)

inputLogin = driver.find_element(By.ID, "user-name").send_keys("standard_user")

inputPass = driver.find_element(By.ID, "password").send_keys("secret_sauce")

btnLogin = driver.find_element(By.ID, "login-button").click()

products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

print("Found " + str(len(products)) + " products:")

for product in products:
    print(product.text)

driver.quit()