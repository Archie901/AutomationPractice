import requests
import json
import time
import _main
import adata as ad
from dev_authorization import access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + access_token}

def create_template():
    payloadCreate = {
    "template": {
        "title": ad.Methods.randomizer(ad.QRtemp.templateNames),
        },
        "logoSize": 20,
        "frameTextSize": ad.Methods.randomizer(ad.QRtemp.sizes),
		"frameText": ad.Methods.randomizer(ad.QRtemp.frameTexts),		
		"frameTextColor": ad.Methods.randomizer(ad.General.mediumColors),
		"frameBackgroundColor": ad.Methods.randomizer(ad.General.darkColors),
		"backgroundColor": ad.Methods.randomizer(ad.General.lightColors),
		"patternColor": ad.Methods.randomizer(ad.General.darkColors),
		"cornerColor": ad.Methods.randomizer(ad.General.darkColors),
		"frameType": ad.Methods.randomizer(ad.QRtemp.frameTypes),
		"patternType": ad.Methods.randomizer(ad.QRtemp.patternTypes),
		"cornerType": ad.Methods.randomizer(ad.QRtemp.cornerTypes),
        "libraryId": ad.Methods.randomizer(ad.QRtemp.library_ids),
    }
    payload_json = json.dumps(payloadCreate)
    resp_create = requests.post(url=ad.Requests.dev_api_domain+ad.Requests.path_tempCreate,
                                data=payload_json, headers=headersToken)
    #print(resp_create.text)
    print("create request:", resp_create.status_code, "/", resp_create.reason, "/", resp_create.elapsed)    
    assert resp_create.status_code == 200, "status code not 200"
    assert resp_create.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_create.json()['id'] != None, "required id field value empty"
    assert resp_create.json()['createdDate'] != None, "required createdDate field value empty"

iterations = 15

count = 0
while True:
    count += 1
    create_template()
    if count == iterations:
        break