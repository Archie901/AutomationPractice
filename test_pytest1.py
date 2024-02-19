import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from typing import List

'''class TestSomething():

    @pytest.fixture()
    def test_setup(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://www.saucedemo.com")
        yield
        self.driver.close()
        
    def test_login(self, test_setup):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        x = self.driver.title
        assert x == "Swag Labs", "TITLE IS DIFFERENT"
        time.sleep(2)
        print("Test completed")

    if __name__ == "__main__":
        pytest.main(["-s", "-v" ,"pytest_test.py"])'''

def total(xs: List[float]) -> float:
    '''Total returns the sums of xs.'''
    result: float = 0.0
    #For each x float in xs, add it to result
    for x in xs:
        result += x
    return result

def join(xs: List[int], delimiter: str) -> str:
    '''Produce a string where subsequent items are separated by delimiter'''
    generated_string: str = ""
    for x in xs:
        if generated_string == "":               #do not put delimiter before the first item
            generated_string = str(x)
        else:
            generated_string += delimiter + str(x)
    return generated_string
    