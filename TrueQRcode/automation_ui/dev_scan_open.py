import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import _main
import adata as ad

#service = Service()

#options = webdriver.ChromeOptions()

#driver = webdriver.Chrome(service=service, options=options)

driver = webdriver.Edge()

#driver = webdriver.Firefox()

iterations = 2

count = 0
while True:
    qrId = ad.Methods.randomizer(ad.QRids.dev_qrIds_Newest)
    print(qrId)
    count += 1
    driver.get(ad.Requests.dev_url_domain + "/qr/" + qrId)
    time.sleep(6)
    if count == iterations:
        break

driver.quit()