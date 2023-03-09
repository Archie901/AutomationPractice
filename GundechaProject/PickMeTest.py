import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(2)
        cls.driver.get("https://www.saucedemo.com")
    def test1_login_toPage(self):
        logo = self.driver.find_element(By.CLASS_NAME, "login_logo")
        self.assertTrue(logo)
        print(logo.text)
        inputLogin = self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        inputPass = self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        btnLogin = self.driver.find_element(By.ID, "login-button").click();
    def test2_sortingThings(self):
        self.assertTrue(self.driver.find_element(By.XPATH, "//span[text()='Products']"))
        sortingDropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        selected_option = sortingDropdown.first_selected_option
        print(selected_option.text)
    def test3_clickingBurger(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "react-burger-cross-btn").click()
    def test4_whetherCartEmpty(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
        try:
            self.driver.find_element(By.XPATH, "//div[@class='cart_list']//div[@class='cart_item']")
            print("Element is present")
        except NoSuchElementException:
            print("Element is NOT present")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
