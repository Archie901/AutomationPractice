import requests
import json
import time
from adata import Requests, QRcodes_Templates
import dev_authorization

token = dev_authorization.access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + token}

def create_template():
    payloadCreate = {
    "template": {
        "title": QRcodes_Templates.randomTemplateName(),
        },
    "libraryId": None,
    "logoSize": 20,
	"frameText": QRcodes_Templates.randomFrameText(),
	"frameTextSize": 12,
	"frameTextColor": "#000000",
	"frameBackgroundColor": "#000000",
	"backgroundColor": QRcodes_Templates.randomBackColor(),
	"patternColor": QRcodes_Templates.randomPatternColor(),
	"cornerColor": QRcodes_Templates.randomCornerColor(),
	"frameType": QRcodes_Templates.randomFrameType(),
	"patternType": QRcodes_Templates.randomPatternType(),
	"cornerType": QRcodes_Templates.randomCornerType()
    }
    payload_json = json.dumps(payloadCreate)
    resp_create = requests.post(url=Requests.dev_api_domain+Requests.path_tempCreate, data=payload_json, headers=headersToken)
    print("create request:", resp_create.status_code, "/", resp_create.reason, "/", resp_create.elapsed)
    #print(resp_create.text)
    assert resp_create.status_code == 200, "status code not 200"
    assert resp_create.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_create.json()['id'] != None, "required field value empty"
    assert resp_create.json()['createdDate'] != None, "required field value empty"

iterations = 6

count = 0
while True:
    count += 1
    create_template()
    if count == iterations:
        break