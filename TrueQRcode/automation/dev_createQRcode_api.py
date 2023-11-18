import requests
import json
import time
from adata import Requests, QRcodes
import dev_authorization

token = dev_authorization.access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + token}

def create_qr_code():
    payloadCreate = {
    "codeType": "WEBSITE",
	"name": QRcodes.randomQRname(),
	"design": {
		"logoSize": 20,
		"frameText": QRcodes.randomFrameText(),
		"frameTextSize": 12,
		"frameTextColor": "#000000",
		"frameBackgroundColor": "#000000",
		"backgroundColor": QRcodes.randomBackColor(),
		"patternColor": QRcodes.randomPatternColor(),
		"cornerColor": QRcodes.randomCornerColor(),
		"frameType": QRcodes.randomFrameType(),
		"patternType": QRcodes.randomPatternType(),
		"cornerType": QRcodes.randomCornerType()
        },
	"website": {
		"url": QRcodes.randomTargetUrl()
        }
    }
    payload_json = json.dumps(payloadCreate)
    resp_create = requests.post(url=Requests.dev_api_domain+Requests.path_qrCreate, data=payload_json, headers=headersToken)
    print(resp_create.status_code, "/", resp_create.reason, "/", resp_create.elapsed)
    assert resp_create.status_code == 200, "status code not 200"
    assert resp_create.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_create.json()['id'] != None, "required field value empty"
    assert resp_create.json()['name'] != None, "required field value empty"
    assert resp_create.json()['codeType'] != None, "required field value empty"
    #print(resp_create.text)

iterations = 1

count = 0
while True:
    count += 1
    create_qr_code()
    if count == iterations:
        break