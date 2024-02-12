import requests
import json
import random
import pytest
from data import Requests, Creds

def randomizer(x):
    randomed = random.choice(x)
    return randomed

@pytest.fixture(scope='session')
def login():
    customer_email = Creds.dev_customerCreds[8][0]
    customer_password = Creds.dev_customerCreds[8][1]
    payload_login = {"authType": "TOKEN", "email": customer_email, "password": customer_password}
    payload_json = json.dumps(payload_login)
    resp_login = requests.post(url=Requests.dev_api_domain+Requests.path_login, data=payload_json, headers=Requests.headers)
    #print(resp_login.text)
    print("login request:", resp_login.status_code, "/", resp_login.reason, "/", resp_login.elapsed)
    print("email from login response:", f"-- {resp_login.json()["email"]} --")
    assert resp_login.status_code == 200, "status code not 200"
    assert resp_login.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_login.json()['email'] == customer_email, "email does not match"
    assert resp_login.json()['id'] != None, "required id field value empty"
    assert resp_login.json()['role'] != None, "required role field value empty"
    pytest.user_id = resp_login.json()['id']
    pytest.user_email = resp_login.json()['email']
    access_token = resp_login.json()["accessToken"]
    pytest.headersToken = {
        "Content-Type": "application/json",
        "Accept-Encoding": "charset=utf-8",
        "Connection": "keep-alive",
        "Authorization": "Bearer " + access_token
    }