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
    	#{"linkType": "TIKTOK", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"},
    	{"linkType": "TELEGRAM", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"},
    	#{"linkType": "WHATSAPP", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"},
    	#{"linkType": "INSTAGRAM", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"},
    	{"linkType": "YOUTUBE", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"},
    	{"linkType": "TWITTER", "url": Methods.randomizer(QRcodes_Templates.targetURLs), "title": "social"}
    ]
    payloadCreate = {
    "codeType": "V_CARD",
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
	"vcard": {
		"designPrimaryColor": Methods.randomizer(QRcodes_Templates.darkColors),
		"designSecondaryColor": Methods.randomizer(QRcodes_Templates.lightColors),
		"designNameColor": Methods.randomizer(QRcodes_Templates.lightColors),
		"designTextColor": Methods.randomizer(QRcodes_Templates.darkColors),
		"designIconColor": Methods.randomizer(QRcodes_Templates.mediumColors),
		"designTextHoverColor": Methods.randomizer(QRcodes_Templates.mediumColors),
		"designTitleColor": Methods.randomizer(QRcodes_Templates.darkColors),
		"buttonText": "Add Contact",
		"buttonSize": 14,
		"buttonBgColor": Methods.randomizer(QRcodes_Templates.lightColors),
		"buttonTextColor": Methods.randomizer(QRcodes_Templates.darkColors),
		"buttonHoverColor": Methods.randomizer(QRcodes_Templates.mediumColors),
		"buttonBorderColor": Methods.randomizer(QRcodes_Templates.darkColors),
		"fullName": "Person Aboutall",
		"phoneNumber": "+385915981787",
		"alternativePhoneNumber": "+385915981787",
		"email": "xedyx@mailinator.com",
		"website": Methods.randomizer(QRcodes_Templates.targetURLs),
		"companyName": "Very important vernture.LTD",
		"jobPosition": "senior assistant of helper",
		"street": "541 Kometensingel",
		"postalCode": "1033 BR",
		"city": "Amsterdam",
		"state": "North Holland",
		"country": "Netherlands",
		"links": socialLinks,
		"libraryId": Methods.randomizer(QRcodes_Templates.library_ids)
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

iterations = 1

count = 0
while True:
    count += 1
    create_qr_code()
    if count == iterations:
        break