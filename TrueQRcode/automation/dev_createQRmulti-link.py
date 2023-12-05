import requests
import json
import time
from adata import Requests, QRcodes_Templates, Methods
import dev_authorization

token = dev_authorization.access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + token}

def create_qr_code():
    socialLinks = [
    	{"linkType": "FACEBOOK", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"},
    	{"linkType": "LINKEDIN", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"},
    	{"linkType": "TIKTOK", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"},
    	{"linkType": "TELEGRAM", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"},
    	{"linkType": "WHATSAPP", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"},
    	{"linkType": "INSTAGRAM", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"},
    	{"linkType": "YOUTUBE", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"},
    	{"linkType": "TWITTER", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"}
    ]
    customLinks = [
        {"library": {}, "libraryId": Methods.randomizer(QRcodes_Templates.library_ids),
         "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": Methods.randomizer(QRcodes_Templates.AddNames), "linkType": "CUSTOM"},
        {"library": {}, "libraryId": Methods.randomizer(QRcodes_Templates.library_ids),
         "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": Methods.randomizer(QRcodes_Templates.AddNames), "linkType": "CUSTOM"},
        {"library": {}, "libraryId": Methods.randomizer(QRcodes_Templates.library_ids),
         "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": Methods.randomizer(QRcodes_Templates.AddNames), "linkType": "CUSTOM"},
        ]
    payloadCreate = {
    "codeType": "MULTILINK",
	"name": Methods.randomizer(QRcodes_Templates.QRnames),
	"design": {
		"logoSize": 20,
        "frameTextSize": 12,
		"frameText": Methods.randomizer(QRcodes_Templates.frameTexts),		
		"frameTextColor": Methods.randomizer(QRcodes_Templates.mediumColors),
		"frameBackgroundColor": Methods.randomizer(QRcodes_Templates.darkColors),
		"backgroundColor": Methods.randomizer(QRcodes_Templates.lightColors),
		"patternColor": Methods.randomizer(QRcodes_Templates.darkColors),
		"cornerColor": Methods.randomizer(QRcodes_Templates.darkColors),
		"frameType": Methods.randomizer(QRcodes_Templates.frameTypes),
		"patternType": Methods.randomizer(QRcodes_Templates.patternTypes),
		"cornerType": Methods.randomizer(QRcodes_Templates.cornerTypes),
        "libraryId": Methods.randomizer(QRcodes_Templates.library_ids)
        },
    "multilink": {
        "socialLinks": socialLinks,
        "customLinks": customLinks,
        "buttonBgColor": Methods.randomizer(QRcodes_Templates.lightColors),
		"buttonTextColor": Methods.randomizer(QRcodes_Templates.darkColors),
		"buttonHoverColor": Methods.randomizer(QRcodes_Templates.mediumColors),
		"buttonBorderColor": Methods.randomizer(QRcodes_Templates.darkColors),
		"designDescriptionColor": Methods.randomizer(QRcodes_Templates.lightColors),
		"designTitleColor": Methods.randomizer(QRcodes_Templates.lightColors),
		"designBgColor": Methods.randomizer(QRcodes_Templates.darkColors),
		"libraryId": Methods.randomizer(QRcodes_Templates.library_ids),
		"description": "Sequi ipsam",
		"title": "Adipisicing dolor"
        },
    }
    payload_json = json.dumps(payloadCreate)
    resp_create = requests.post(url=Requests.dev_api_domain+Requests.path_qrCreate, data=payload_json, headers=headersToken)
    print("create request:", resp_create.status_code, "/", resp_create.reason, "/", resp_create.elapsed)
    #print(resp_create.text)
    assert resp_create.status_code == 200, "status code not 200"
    assert resp_create.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_create.json()['id'] != None, "required field value empty"
    assert resp_create.json()['name'] != None, "required field value empty"
    assert resp_create.json()['codeType'] != None, "required field value empty"

iterations = 5

count = 0
while True:
    count += 1
    create_qr_code()
    if count == iterations:
        break