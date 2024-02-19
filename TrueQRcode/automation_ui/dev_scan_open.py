import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from adata import Methods, QRids, Requests

service = Service()

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

#driver = webdriver.Edge()

#driver = webdriver.Firefox()

iterations = 4

count = 0
while True:
    qrId = Methods.randomizer(QRids.dev_qrIds_Newest)
    print(qrId)
    count += 1
    driver.get(Requests.dev_url_domain + "/qr/" + qrId)
    time.sleep(6)
    if count == iterations:
        break

driver.quit()