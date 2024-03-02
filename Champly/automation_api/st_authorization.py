import requests
import json
import _main
import appdata as ap

def login():
    #user_email = ap.Creds.stage_superCreds[0]
    #user_password = ap.Creds.stage_superCreds[1]
    user_email = ap.Creds.stage_adminCreds[0][0]
    user_password = ap.Creds.stage_adminCreds[0][1]
    payload_login = {"email": user_email, "password": user_password}
    payload_json = json.dumps(payload_login)
    resp_login = requests.post(url=ap.Requests.stage_api_domain+ap.Requests.path_login,
                               data=payload_json, headers=ap.Requests.headers)
    print(resp_login.text)
    print("login request:", resp_login.status_code, "/", resp_login.reason, "/", resp_login.elapsed)
    print("email from login response:", f"-- {resp_login.json()["user"]["email"]} --")
    assert resp_login.status_code == 200, "status code not 200"
    assert resp_login.headers['Content-Type'] == "application/json; charset=utf-8", "content type different"
    assert resp_login.json()["user"]["email"] == user_email, "email does not match"
    assert resp_login.json()["user"]['id'] != None, "required id field value empty"
    assert resp_login.json()["user"]['roleId'] != None, "required role field value empty"
    global access_token
    access_token = resp_login.json()["accessToken"]
    print(access_token)
    
login()