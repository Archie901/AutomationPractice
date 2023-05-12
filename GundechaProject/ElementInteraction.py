import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class FillingTheForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/automation-practice-form")
        #self.driver.execute_script("document.body.style.zoom='100%'")
    def test1_formInputsAndOther(self):
        driver = self.driver
        title_of_form = driver.find_element(By.CSS_SELECTOR, "div.practice-form-wrapper > h5").text
        print(title_of_form)
        self.assertEqual("Student Registration Form", title_of_form)
        input_FirstName = driver.find_element(By.CSS_SELECTOR, "input#firstName")
        input_LastName = driver.find_element(By.CSS_SELECTOR, "input#lastName")
        input_Email = driver.find_element(By.CSS_SELECTOR, "input#userEmail")
        input_Mobile = driver.find_element(By.CSS_SELECTOR, "input#userNumber")
        textArea_Address = driver.find_element(By.CSS_SELECTOR, "textarea#currentAddress")
        checkbox_GenderMale = driver.find_element(By.XPATH, "//label[text()='Male']") 
        btn_submit = driver.find_element(By.XPATH, "//div//button[text()='Submit']")
        self.assertEqual("10", input_Mobile.get_attribute("minlength"))
        self.assertEqual("10", input_Mobile.get_attribute("maxlength"))
        print("Minlength is " + input_Mobile.get_attribute("minlength"), "Maxlength is " + input_Mobile.get_attribute("maxlength"))
        self.assertTrue(input_FirstName and input_LastName and input_Email and input_Mobile and textArea_Address and checkbox_GenderMale)
        input_FirstName.send_keys("AnotherOne")
        input_LastName.send_keys("Copitalist")
        input_Email.send_keys("piece@mailinator.com")
        input_Mobile.send_keys("3809744533")
        textArea_Address.send_keys("One mornn his aoh the size of the rest of him, waved about helplessly as he looked.")
        checkbox_GenderMale.click()
        time.sleep(1)
        self.driver.get("https://demoqa.com/webtables")
        exp_options = ["5 rows", "10 rows", "20 rows", "25 rows", "50 rows", "100 rows"]
        act_options = []
        dropdown = Select(self.driver.find_element(By.TAG_NAME, "select"))
        self.assertEqual(6, len(dropdown.options))
        for option in dropdown.options:
            print(option.text)
        for option in dropdown.options:
            act_options.append(option.text)
        self.assertListEqual(exp_options, act_options)
        self.assertEqual("10 rows", dropdown.first_selected_option.text)
        print(dropdown.first_selected_option.text)
        dropdown.select_by_visible_text("50 rows")
        self.assertEqual("50 rows", dropdown.first_selected_option.text)
        print(dropdown.first_selected_option.text)
        dropdown.select_by_index(0)
        self.assertEqual("5 rows", dropdown.first_selected_option.text)
        print(dropdown.first_selected_option.text)
        self.driver.get("https://demoqa.com/alerts")
        click_me_btn = self.driver.find_element(By.CSS_SELECTOR, "button#alertButton")
        click_me_btn.click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        self.assertEqual("You clicked a button", alert_text)
        alert.accept()
        time.sleep(1)
        frames_btn = self.driver.find_element(By.XPATH, "//li[@id='item-2']//span[text()='Frames']")
        frames_btn.click()
        time.sleep(1)
        self.driver.back()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(expected_conditions.url_matches("https://demoqa.com/alerts"))
        print(element, type(element))
        self.assertTrue(element)
        time.sleep(1)
        self.driver.forward()
        time.sleep(1)
        element2 = wait.until(expected_conditions.url_matches("https://demoqa.com/frames"))
        print(element, type(element2))
        self.assertTrue(element2)
        time.sleep(1)
        self.driver.refresh()
        print(element, type(element2))
        self.assertTrue(element2)
        time.sleep(1)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
