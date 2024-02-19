import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from page_login import PageLogin
from page_profile import PageProfile
from test_data import TestData

'''In test objects we should (for unittest) make setUp and tearDown and write our test'''

class AllTestsHere(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get(TestData.login_url)
    
    def test1_valid_creds(self):
        login_things = PageLogin(self.driver)
        login_things.set_email_in_field(TestData.email)
        login_things.set_password_in_field(TestData.password)
        login_things.click_login_button()
        time.sleep(2)
        logo_image = PageProfile(self.driver).profile_logo_fullLocator()
        try:
            self.assertTrue(logo_image.is_displayed)
            print("the logo image found")
        except NoSuchElementException:
            print("the image is not found")
        userName_profile = PageProfile(self.driver).userName_value_text()
        print(userName_profile + " / " + TestData.email)
        self.assertEqual(userName_profile, TestData.email)
            
    def tearDown(self):
        self.driver.close()
        
if __name__ =="__main__":
    unittest.main()