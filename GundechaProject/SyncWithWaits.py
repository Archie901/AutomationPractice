import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class ExplicitWaitTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        
    '''def test1_searchingProcess(self):
        self.driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(self.driver, 10)
        print(type(wait), wait)
        input_login = self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Username']")
        input_password = self.driver.find_element(By.XPATH, "//input[@type='password' and @placeholder='Password']")
        log_btn = self.driver.find_element(By.ID, "login-button")
        wait.until(expected_conditions.visibility_of((input_login)))
        wait.until(expected_conditions.visibility_of((input_password)))
        wait.until(expected_conditions.element_to_be_clickable((log_btn)))
        log_btn.click()
        time.sleep(2)'''
    
    def test2_checkingAlerts(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://demoqa.com/alerts")
        span_text = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Click Button')]")
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Click Button')]")))
        print(span_text.text)
        alert_btn = self.driver.find_element(By.ID, "alertButton")
        alert_btn.click()
        wait.until(expected_conditions.alert_is_present())
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        self.assertEqual("You clicked a button", alert_text)
        alert.accept()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
