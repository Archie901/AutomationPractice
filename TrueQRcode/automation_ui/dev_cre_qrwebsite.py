import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import _main
import adata as ad
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Edge()
#driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://dev.trueqrcode.com/auth/sign-in")
email_input = driver.find_element(By.XPATH, '//input[@name="email"]')
time.sleep(1)
email_input.send_keys("newest@mailinator.com")
password_input = driver.find_element(By.XPATH, '//input[@name="password"]')
driver.implicitly_wait(2)
password_input.send_keys("Qwerty123!")
time.sleep(1)
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_button.click()
time.sleep(1)
dashboard_side = driver.find_element(By.XPATH, '//span[contains(text(),"Dashboard")]')
print(dashboard_side.text)
create_qr_button = driver.find_element(By.XPATH, '//span[contains(text(), "Create")]')
create_qr_button.click()
time.sleep(1)
next_button = driver.find_element(By.XPATH, '//button//span[1][contains(text(), "Next")]')
next_button.click()
time.sleep(1)
website_input = driver.find_element(By.XPATH, '//input[@name="websiteUrl"]')
website_input.send_keys("http://example.com/")
next_button.click()
time.sleep(1)

frame_button = driver.find_element(By.XPATH, '//div[contains(text(), "Frame")]')

frame_button.click()
time.sleep(1)

random_digits = (9, 10)

randomed = ad.Methods.randomizer(random_digits)

frame_container1 = driver.find_element(By.XPATH, f'//div[contains(@class, "grid")][1]//div[{randomed}]//div[1][contains(@class, "FrameContainer_container")]')

frame_container1.click()
time.sleep(1)
frame_container1.click()
time.sleep(1)
frame_container1.click()
time.sleep(1)
frame_container1.click()
time.sleep(1)
frame_container1.click()
time.sleep(1)

'''next_button.click()
time.sleep(2)
confirm_save_button = driver.find_element(By.XPATH, '//button//span[1][contains(text(), "Confirm")]')
confirm_save_button.click()
time.sleep(4)
website_of_code_created = driver.find_element(By.XPATH, '//span[contains(text(), "http://example.com/")]')
print(website_of_code_created.text)'''

driver.quit()