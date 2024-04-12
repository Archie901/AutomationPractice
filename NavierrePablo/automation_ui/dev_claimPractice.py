import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#service = Service()

#options = webdriver.ChromeOptions()

#driver = webdriver.Chrome(service=service, options=options)

#driver = webdriver.Edge()

driver = webdriver.Firefox()

wait = WebDriverWait(driver, 10)

driver.get("https://pablo-dev.vercel.app/for-providers/claim")

claim_button = driver.find_element(By.XPATH, '//button[contains(text(),"Claim Business")]')

wait.until(expected_conditions.visibility_of((claim_button)))

claim_button.click()

driver.implicitly_wait(2)

all_lvl1_elements = driver.find_elements(By.XPATH, "//div/button/p[contains(@class, 'MuiTypography-body1 grow')]")

print(all_lvl1_elements)

def randomizer(x):
    randomed = random.choice(x)
    return randomed

random_element = randomizer(all_lvl1_elements)

print(random_element)

#button_lvl1 = driver.find_element(By.XPATH, "//div/button/p[contains(@class, 'MuiTypography-body1 grow')]")

time.sleep(1)

random_element.click()

time.sleep(1)

'''button_lvl2 = driver.find_element(By.XPATH, "//button/p[contains(text(), '" +_experiments.random_lvl2['title']+ "')]")

time.sleep(2)'''


'''
inpatient_buttonlevel3_2 = driver.find_element(By.XPATH, "//button/p[contains(text(), 'Inpatient Units')]")
inpatient_buttonlevel3_3 = driver.find_element(By.XPATH, "//button/p[contains(text(), 'Laboratory Department')]")
inpatient_buttonlevel3_4 = driver.find_element(By.XPATH, "//button/p[contains(text(), 'Imaging Department')]")

wait.until(expected_conditions.visibility_of((inpatient_buttonlevel3_1)))
wait.until(expected_conditions.visibility_of((inpatient_buttonlevel3_2)))
wait.until(expected_conditions.visibility_of((inpatient_buttonlevel3_3)))
wait.until(expected_conditions.visibility_of((inpatient_buttonlevel3_4)))

inpatient_buttonlevel3_1.click()
inpatient_buttonlevel3_2.click()
inpatient_buttonlevel3_3.click()
inpatient_buttonlevel3_4.click()

time.sleep(1)

continue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]")

continue_button.click()

time.sleep(1)

continue_button2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]")

continue_button2.click()

time.sleep(1)

if driver.find_element(By.XPATH, "//span[contains(text(), '" +Tex1+ "')]"):
    print("Element exists! - 1")'''

driver.quit()