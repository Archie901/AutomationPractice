import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import _main
import atestus as at

service = Service()
options = webdriver.ChromeOptions()
options.set_capability("goog:loggingPrefs", {"browser": "SEVERE"})
driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Edge()
#driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

def test_intiation():
    driver.get(at.Requests.devstage_pablo_url_domain + "/for-providers/claim")
    driver.implicitly_wait(3)
    busi_claim_button = driver.find_element(By.XPATH, f'{at.BusiMainPage.busi_claim_button}')
    wait.until(expected_conditions.visibility_of((busi_claim_button)))
    busi_claim_button.click()
    time.sleep(2)
    inpatient_button = driver.find_element(By.XPATH, f'{at.BusiMainPage.inpatient_button}')
    inpatient_button.click()
    time.sleep(1)