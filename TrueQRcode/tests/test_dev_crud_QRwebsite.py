import requests
import json
from tdata import Requests, QRcodes_Templates

def test_create_qr_code():
    payloadCreate = {
    "codeType": "WEBSITE",
	"name": QRcodes_Templates.randomQRname(),
	"design": {
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
        },
	"website": {
		"url": QRcodes_Templates.randomTargetUrl()
        }
    }
    payload_json = json.dumps(payloadCreate)
    headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
           "Connection": "keep-alive", "Authorization": "Bearer " + Requests.access_token}
    resp_create = requests.post(url=Requests.dev_api_domain+Requests.path_qrCreate, data=payload_json, headers=headersToken)
    print("create request:", resp_create.status_code, "/", resp_create.reason, "/", resp_create.elapsed)
    #print(resp_create.text)
    assert resp_create.status_code == 200, "status code not 200"
    assert resp_create.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_create.json()['id'] != None, "required field value empty"
    assert resp_create.json()['name'] != None, "required field value empty"
    assert resp_create.json()['codeType'] != None, "required field value empty"
    assert resp_create.json()['amountOfScans'] == 0, "initial scans not 0"
    assert resp_create.json()['totalDownloads'] == 0, "initial downloads not 0"    
    global cre_qr_id, cre_qr_name, cre_qr_type, cre_amountOfScans, cre_totalDownloads
    cre_qr_id = resp_create.json()['id']
    cre_qr_name = resp_create.json()['name']
    cre_qr_type = resp_create.json()['codeType']
    cre_amountOfScans = resp_create.json()['amountOfScans']
    cre_totalDownloads = resp_create.json()['totalDownloads']

def test_check_qr_code():
    headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
           "Connection": "keep-alive", "Authorization": "Bearer " + Requests.access_token}
    resp_qrSingle = requests.get(url=Requests.dev_api_domain+Requests.path_qrSingle+cre_qr_id, headers=headersToken)
    print("get qr request:", resp_qrSingle.status_code, "/", resp_qrSingle.reason, "/", resp_qrSingle.elapsed)
    #print(resp_qrSingle.text)
    assert resp_qrSingle.status_code == 200, "status code not 200"
    assert resp_qrSingle.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_qrSingle.json()['id'] == cre_qr_id, "qr id does not match"
    assert resp_qrSingle.json()['name'] == cre_qr_name, "qr name does not match"
    assert resp_qrSingle.json()['codeType'] == cre_qr_type, "qr type does not match"
    assert resp_qrSingle.json()['amountOfScans'] == cre_amountOfScans, "initial scans not 0"
    assert resp_qrSingle.json()['totalDownloads'] == cre_totalDownloads, "initial downloads not 0"
    
# cd TrueQRcode/tests
# pytest test_dev_QRcrud.py -s -vv
# pytest --count=10 test_dev_QRcrud.py -s -vv