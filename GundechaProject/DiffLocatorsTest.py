import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class LocatorsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(2)        
        cls.driver.get("https://demoqa.com/")
    def test1_ID(self):
        driver = self.driver
        idApp = driver.find_element(By.ID, "app")
        print(type(idApp))
        self.assertTrue(driver.find_element(By.ID, "app"))
    def test2_Class(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//div[@class='card mt-4 top-card'][1]").click()
        driver.find_element(By.XPATH, "//li[@class='btn btn-light '][1]").click()
        usernameField = driver.find_element(By.ID, "userName")
        self.assertEqual("Full Name", usernameField.get_attribute('placeholder'))
    @unittest.skip("demonstrating skipping")
    def test3_IDRadio(self):
        driver = self.driver
        driver.find_element(By.ID, "item-2").click()
        driver.find_element(By.XPATH, "//label[text()='Yes']").click()
        self.assertTrue("text-success", driver.find_element(By.XPATH, "//span[text()='Yes']").get_attribute('class'))
    def test4_LinkFull(self):
        driver = self.driver
        driver.find_element(By.ID, "item-5").click()
        accountLink = driver.find_element(By.LINK_TEXT, 'Moved').click()
        print(accountLink)
    def test5_LinkPartial(self):
        driver = self.driver
        driver.find_element(By.ID, "item-5").click()
        anotherLink = driver.find_element(By.PARTIAL_LINK_TEXT, 'Forbid').click()
        print(anotherLink)
        links = driver.find_elements(By.TAG_NAME, 'p>a')
        print(links)
        self.assertTrue(9, len(links))
    def test6_Tag(self):
        driver = self.driver
        driver.find_element(By.ID, "item-4").click()
        btns = driver.find_elements(By.TAG_NAME, 'button')
        self.assertEqual(4, len(btns))
    def test7_CSS_selector(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//span[contains(text(), 'Images')]").click()
        image = driver.find_element(By.CSS_SELECTOR, "img[src='/images/Toolsqa.jpg']")
        try:
            self.assertTrue(image.is_displayed)
            print("the first image found")
        except NoSuchElementException:
            print("the image is not found")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
