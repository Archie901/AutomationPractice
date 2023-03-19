import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestParallel(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor = "http://192.168.56.1:4444",
            desired_capabilities = {
                "browserName": "Firefox"
            }
        )
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test1(self):
        self.driver.get("https://demoqa.com/")
        time.sleep(2)

    def test2(self):
        self.driver.get("https://qa.bettin.gs/dashboard/statistics")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
