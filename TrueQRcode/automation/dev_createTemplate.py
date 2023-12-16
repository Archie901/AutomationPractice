import requests
import json
import time
from adata import Requests, QRtemp, General, Methods
import dev_authorization

token = dev_authorization.access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + token}

def create_template():
    payloadCreate = {
    "template": {
        "title": Methods.randomizer(QRtemp.templateNames),
        },
        "logoSize": 20,
        "frameTextSize": Methods.randomizer(QRtemp.sizes),
		"frameText": Methods.randomizer(QRtemp.frameTexts),		
		"frameTextColor": Methods.randomizer(General.mediumColors),
		"frameBackgroundColor": Methods.randomizer(General.darkColors),
		"backgroundColor": Methods.randomizer(General.lightColors),
		"patternColor": Methods.randomizer(General.darkColors),
		"cornerColor": Methods.randomizer(General.darkColors),
		"frameType": Methods.randomizer(QRtemp.frameTypes),
		"patternType": Methods.randomizer(QRtemp.patternTypes),
		"cornerType": Methods.randomizer(QRtemp.cornerTypes),
        "libraryId": Methods.randomizer(QRtemp.library_ids),
    }
    payload_json = json.dumps(payloadCreate)
    resp_create = requests.post(url=Requests.dev_api_domain+Requests.path_tempCreate, data=payload_json, headers=headersToken)
    #print(resp_create.text)
    print("create request:", resp_create.status_code, "/", resp_create.reason, "/", resp_create.elapsed)    
    assert resp_create.status_code == 200, "status code not 200"
    assert resp_create.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_create.json()['id'] != None, "required field value empty"
    assert resp_create.json()['createdDate'] != None, "required field value empty"

iterations = 5

count = 0
while True:
    count += 1
    create_template()
    if count == iterations:
        break