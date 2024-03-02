import requests
import json
import time
import _main
import appdata as ap
from st_authorization import access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + access_token}

def create_user():
    #"roleId": 1, 2, 3, 4 === superuser, admin, manager, member
    payloadCreate = {
        "orgId": ap.Requests.org_id,
        "roleId": ap.Methods.randomizer([2, 3, 4]),
        "email": ap.Methods.randomizer(ap.General.emails2),
        "password": "Qwerty123!",
        "phone": "+1 438-482-8066",
        "firstName": ap.Methods.randomizer(ap.General.firstNames),
        "lastName": ap.Methods.randomizer(ap.General.lastNames),
        "title": ap.Methods.randomizer(ap.General.titles),
        "linkedin": ap.Methods.randomizer(ap.General.weblinks),
		"teamId": 87
    }
    payload_json = json.dumps(payloadCreate)
    resp_create = requests.post(url=ap.Requests.stage_api_domain+ap.Requests.path_users,
                               data=payload_json, headers=headersToken)
    print(resp_create.text)
    print("create request:", resp_create.status_code, "/", resp_create.reason, "/", resp_create.elapsed)
    assert resp_create.status_code == 200, "status code not 200"
    assert resp_create.headers['Content-Type'] == "application/json; charset=utf-8", "content type different"
    assert resp_create.json()['id'] != None, "required id field value empty"
    assert resp_create.json()['email'] != None, "required name field value empty"
    assert resp_create.json()['roleId'] != None, "required codeType field value empty"

iterations = 5

count = 0
while True:
    count += 1
    create_user()
    if count == iterations:
        break