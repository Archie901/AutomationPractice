import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class SearchProductsOnAndroid(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11.0'
        desired_caps['browserName'] = 'Chrome'
        desired_caps['androidInstallTimeout'] = 90000
        self.driver = \
            webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.get("https://demoqa.com/text-box")
        self.driver.implicitly_wait(10)

    def test_searchingAndFilling(self):
        elements = self.driver.find_elements(By.XPATH, "//div[@class='element-group']")
        print(elements)
        self.driver.find_element(By.ID, "userName").send_keys("Lorem ipsum dolormperdiet. Etiam ul")
        self.driver.find_element(By.ID, "userEmail").send_keys("something@mailinator.com")
        self.driver.find_element(By.ID, "currentAddress").send_keys("aecenas tempus, tellus eget condm sem")
        self.driver.find_element(By.ID, "permanentAddress").send_keys("ris sit amet nibh. Donec sodales sagittis mag")
        self.driver.find_element(By.CSS_SELECTOR, "button#submit").click()
        name_appeared = self.driver.find_element(By.XPATH, "//p[@id='name']")
        email_appeared = self.driver.find_element(By.XPATH, "//p[@id='email']")
        self.assertTrue(name_appeared)
        self.assertTrue(email_appeared)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
