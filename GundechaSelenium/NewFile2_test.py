import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://www.saucedemo.com")
        cls.driver.title
    def test_searchingItems(self):
        inputLogin = self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        inputPass = self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        btnLogin = self.driver.find_element(By.ID, "login-button").click()
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        print(type(products))
        print("Found " + str(len(products)) + " products:")
        for product in products:
            print(product.text)
        self.assertEqual(6, len(products), '332433222222222222222222')
    def test_something_new(self):
        sorting1 = self.driver.find_element(By.XPATH, "//select//option[@value='lohi']").click()
        sorting2 = self.driver.find_element(By.XPATH, "//select//option[@value='za']").click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
