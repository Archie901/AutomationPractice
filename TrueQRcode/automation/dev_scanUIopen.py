import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Trueqrcode.automation.adata import Requests, Scans

service = Service()

options = webdriver.ChromeOptions()

#driver = webdriver.Chrome(service=service, options=options)

driver = webdriver.Edge()

#driver = webdriver.Firefox()

iterations = 10

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