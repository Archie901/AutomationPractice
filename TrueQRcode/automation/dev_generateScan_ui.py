import time
from selenium import webdriver
from data import Requests, Scans, Functions

iterations = 5

driver = webdriver.Firefox()

count = 0
while True:
    random_qrId = Functions.randomizer(Scans.dev_qrIds)
    print(random_qrId)
    count += 1
    driver.get(Requests.dev_url_domain + "/qr/" + random_qrId)
    time.sleep(6)
    if count == iterations:
        break

driver.quit()