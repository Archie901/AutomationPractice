import requests
import json
import time
import _main
import appdata as ap
from st_authorization import access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + access_token}

def create_site():
    payloadCreate = {
        "name": ap.Methods.randomizer(ap.General.phrases),
        "prospectName": ap.Methods.randomizer(ap.General.companies),
        "prospectUrl": ap.Methods.randomizer(ap.General.weblinks),
        "champion": ap.Methods.randomizer(ap.General.firstNames),
        "orgId": 30
    }
    payload_json = json.dumps(payloadCreate)
    resp_create = requests.post(url=ap.Requests.stage_api_domain+ap.Requests.path_sites,
                               data=payload_json, headers=headersToken)
    print(resp_create.text)
    print("create request:", resp_create.status_code, "/", resp_create.reason, "/", resp_create.elapsed)
    assert resp_create.status_code == 200, "status code not 200"
    assert resp_create.headers['Content-Type'] == "application/json; charset=utf-8", "content type different"
    assert resp_create.json()['id'] != None, "required id field value empty"
    assert resp_create.json()['name'] != None, "required name field value empty"
    assert resp_create.json()['champion'] != None, "required codeType field value empty"

iterations = 3

count = 0
while True:
    count += 1
    create_site()
    if count == iterations:
        break