import requests
import json
import random
import pytest

domain = "https://api-dev.trueqrcode.com"

pathLogin = "/api/v1/public/auth/sign-in"

headers = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8", "Connection": "keep-alive"}

customer_creds = (
    ["komic@mailinator.com", "Something555!"],
    ["mykemos@protonmail.com", "Qwerty2233!"],
    ["merkar@mailinator.com", "Something555!"]
)

def randomizer(x):
    return random.choice(x)

def test_login():

    randomCreds = randomizer(customer_creds)
    #print(randomCreds)    
    payloadLogin = {"authType": "TOKEN", "email": randomCreds[0], "password": randomCreds[1]}
    json_payloadLogin = json.dumps(payloadLogin)    
    resp_login = requests.post(url=domain+pathLogin, data=json_payloadLogin, headers=headers)
    print(resp_login.status_code, "/", resp_login.reason, "/", resp_login.elapsed)
    #print(resp_login.text)
    global access_token
    access_token = resp_login.json()["accessToken"]
    #print(access_token)
    assert resp_login.status_code == 200, "status code not 200"
    assert resp_login.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_login.json()["email"] == randomCreds[0], "email does not match"
    assert resp_login.json()['id'] != None, "required field value empty"
    assert resp_login.json()['role'] != None, "required field value empty"

# cd TrueQRcode/_tests
# pytest test_dev_auth.py -s -vv
# pytest --count=5 test_dev_auth.py -s -vv