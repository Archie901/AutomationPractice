import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.set_window_rect(x=500, y=200, width=450, height=500)

    '''def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        time.sleep(1)
        elem.send_keys("pycon")
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        window_pos= driver.get_window_position()
        print(window_pos)
        print(driver.get_window_size())'''

    '''def test_using_iframes(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/html/html_iframe.asp")
        iframe = driver.find_element(By.XPATH, "//iframe[@title='W3Schools HTML Tutorial']")
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, "//iframe//following::a[@href='/css/default.asp']").click()
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, "//a[@href='/css/default.asp']").click()'''

    '''def test_textbox(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")
        textb = driver.find_element(By.ID, "currentAddress")
        textb.send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.\
        Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et m\
        agnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, preti")
        time.sleep(1)
        placeholder = textb.get_attribute("placeholder")
        print(placeholder, type(placeholder))
        self.assertEqual(textb.get_attribute("placeholder"), "Current Address")'''

    def test_dict(self):
        dict1 = {"lang":"python", "tool":"selenium", "publication":"apress", "year":"2020"}
        dict2 = {"lang":"python", "tool":"selenium", "publication":"apress", "year":"2020"}
        self.assertDictEqual(dict1, dict2, "Dictionaries don't Match.")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()