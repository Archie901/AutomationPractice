import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HRMtesting(unittest.TestCase):
    def setUp(self):
        global driver
        self.driver = webdriver.Edge()
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
    def test_hrmLogin_and_other(self):
        inputLogin = driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@name='username' and @placeholder='Username']")
        inputLogin.send_keys("Admin")
        inputPassword = driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@name='password' and @placeholder='Password']")
        inputPassword.send_keys("admin123")
        buttonLogin = driver.find_element(By.XPATH, "//div[@class='oxd-form-actions orangehrm-login-action']//button[@type='submit']")
        buttonLogin.click()
        time.sleep(2)
        pimClickable = driver.find_element(By.XPATH, "//div//ul//li//a[@href='/web/index.php/pim/viewPimModule']")
        pimClickable.click()
        time.sleep(2)
        assert driver.page_source.find("Employee Information")
        buttonAdd = driver.find_element(By.XPATH, "//button[@type='button' and @class='oxd-button oxd-button--medium oxd-button--secondary']")
        buttonAdd.click()
        time.sleep(2)
        x = "1Maorik"
        y = "2Libokin"
        z = "3Vukomur"
        inputFirstName = driver.find_element(By.XPATH, "//input[@name='firstName' and @placeholder='First Name']")
        inputFirstName.send_keys(x)
        inputMiddleName = driver.find_element(By.XPATH, "//input[@name='middleName' and @placeholder='Middle Name']")
        inputMiddleName.send_keys(y)
        inputLastName = driver.find_element(By.XPATH, "//input[@name='lastName' and @placeholder='Last Name']")
        inputLastName.send_keys(z)
        buttonSave = driver.find_element(By.XPATH, "//button[@type='submit' and @class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
        buttonSave.click()
        print(x + y + z)
        time.sleep(5)
        if driver.page_source.find(x + " " + y):
            print("URRARA!")
        else:
            print("pizda....")
        time.sleep(2)
    def tearDown(self):
        driver.close()

if __name__ == "__main__":
    unittest.main()
