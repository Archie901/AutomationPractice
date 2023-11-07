import requests
import json

domain = "https://api-trueqrcode-dev.osdb.io"

pathLogin = "/api/v1/public/auth/sign-in"

headers = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8", "Connection": "keep-alive"}

customer_login = "merkar@mailinator.com"

customer_password = "Something555!"

def login():

    payloadLogin = {"authType": "TOKEN", "email": customer_login, "password": customer_password}

    json_paylodLogin = json.dumps(payloadLogin)

    resp_login = requests.post(url=domain+pathLogin, data=json_paylodLogin, headers=headers)
    global access_token
    access_token = resp_login.json()["accessToken"]
    print(access_token)
    print(resp_login.status_code, resp_login.reason, resp_login.elapsed)
    assert resp_login.status_code == 200, "status code is not 200"
    assert resp_login.reason == "OK", "status message is not OK"
    assert resp_login.json()["email"] == customer_login, "email is different"

login()