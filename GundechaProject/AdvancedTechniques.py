from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import datetime, time
import unittest

class VarionsActions_all_this(unittest.TestCase):

    URL = "https://demoqa.com/frames"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(3)

    '''def test_hotkey(self):
        driver = self.driver
        table = driver.find_element(By.XPATH, "//iframe[@id='frame1']")
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//iframe[@id='frame1']")))
        actions = ActionChains(driver)
        actions.move_to_element(table).click()
        actions.key_down(Keys.LEFT_CONTROL).send_keys('a').perform()
        time.sleep(2)'''
    
    '''def test_tool_tip(self):
        driver = self.driver
        widgets_sidebar = driver.find_element(By.XPATH, "//div[contains(text(), 'Widgets')]")
        widgets_sidebar.click()
        driver.get("https://demoqa.com/tool-tips")
        hoveringArea = driver.find_element(By.ID, "toolTipButton")
        acts = ActionChains(driver)
        acts.move_to_element(hoveringArea).perform()
        wait = WebDriverWait(driver, 10)
        tooltiping = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'You hovered over the Button')]")))
        print(tooltiping.text)
        self.assertEqual("You hovered over the Button", tooltiping.text)
        time.sleep(2)'''
    
    '''def test_drag_n_drop(self):
        driver = self.driver
        driver.get("https://demoqa.com/droppable")
        dragging = driver.find_element(By.ID, "draggable")
        dropping = driver.find_element(By.ID, "droppable")
        acts = ActionChains(driver)
        acts.drag_and_drop(dragging, dropping).perform()
        dropped_text = driver.find_element(By.XPATH, "//div[@id='droppable']//p[text()='Dropped!']")
        time.sleep(2)
        self.assertEqual("Dropped!", dropped_text.text)
        print(dropped_text.text)'''
    
    '''def test_making_screenshot(self):
        driver = self.driver
        try:
            table = driver.find_element(By.XPATH, "//iframe[@id='fr234ame1']")
            self.assertEqual("Promotions", table.text)
        except NoSuchElementException:
            #st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
            driver.save_screenshot('somethg-missing.png')
            raise'''
    
    '''def test_popup_windows(self):
        driver = self.driver
        driver.get("https://demoqa.com/browser-windows")
        parent_window = driver.current_window_handle[0]
        new_window_btn = driver.find_element(By.ID, "messageWindowButton")
        new_window_btn.click()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        driver.switch_to.window(parent_window)'''
    
    def test_cookies(self):
        driver = self.driver
        driver.get("https://demoqa.com/")
        some_cookie = driver.get_cookies()
        print(some_cookie)        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
    