import time
from selenium import webdriver
from adata import Requests, Scans

iterations = 10

driver = webdriver.Firefox()

count = 0
while True:
    qrId = Scans.dev_randomQRid()
    print(qrId)
    count += 1
    driver.get(Requests.dev_url_domain + "/qr/" + qrId)
    time.sleep(6)
    if count == iterations:
        break

driver.quit()