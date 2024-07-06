import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Edge()
#driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://pablo-dev.vercel.app/for-providers/claim")
claim_button = driver.find_element(By.XPATH, '//button[contains(text(),"Providers")]')
wait.until(expected_conditions.visibility_of((claim_button)))
claim_button.click()
driver.implicitly_wait(2)

npi_input = driver.find_element(By.XPATH, '//input[@placeholder="NPI Number"]')

npi_input.send_keys("1447211198")

time.sleep(1)

search_button = driver.find_element(By.XPATH, '//button[contains(text(), "Search")]')
search_button.click()

time.sleep(2)

yes_button = driver.find_element(By.XPATH, '//button[contains(text(), "Yes")]')
yes_button.click()





time.sleep(4)

close_button = driver.find_element(By.XPATH, '//button[contains(text(), "Close")]')
close_button.click()

time.sleep(2)

continue_button1 = driver.find_element(By.XPATH, '//a[contains(text(), "Continue")]')
continue_button1.click()

time.sleep(4)

location1_button = driver.find_element(By.XPATH, '//tbody/tr[1]/td/button[contains(@class, "MuiButtonBase-root")]')
location1_button.click()

continue_button2 = driver.find_element(By.XPATH, '//button[contains(text(), "Continue")]')
continue_button2.click()

time.sleep(4)

skip_button = driver.find_element(By.XPATH, '//button[contains(text(), "Skip")]') 
skip_button.click()
time.sleep(2)

email_input = driver.find_element(By.XPATH, '//input[@id="email"]')
phone_input = driver.find_element(By.XPATH, '//input[@id="phone-number"]')
fax_input = driver.find_element(By.XPATH, '//input[@id="fax-number"]')

email_input.send_keys("ukolo@mailinator.com")
phone_input.send_keys("5518239134")
fax_input.send_keys("9805657280")

continue_button2 = driver.find_element(By.XPATH, '//div[contains(@class, "MuiDialogActions-root")]//button[contains(text(), "Continue")]')
continue_button2.click()

time.sleep(2)

pref_email_box = driver.find_element(By.XPATH, '//div/label[1]/span[contains(@class, "MuiButtonBase-root")]')
pref_fax_box = driver.find_element(By.XPATH, '//div/label[2]/span[contains(@class, "MuiButtonBase-root")]')
pref_email_box.click()
pref_fax_box.click()

continue_button3 = driver.find_element(By.XPATH, '//div[contains(@class, "MuiDialogActions-root")]//button[contains(text(), "Continue")]')
continue_button3.click()

time.sleep(2)

continue_button4 = driver.find_element(By.XPATH, '//div[contains(@class, "MuiDialogActions-root")]//button[contains(text(), "Continue")]')
continue_button4.click()

time.sleep(2)

#verify flow is finished, profile verified, now we go to account creation

driver.quit()