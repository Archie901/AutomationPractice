import requests
import json
from tdata import Requests, Customers, Functions

def test_login():
    random_creds = Functions.randomizer(Customers.dev_customerCreds)
    print(random_creds)
    customer_email = random_creds[0]
    customer_password = random_creds[1]
    payload_login = {"authType": "TOKEN", "email": customer_email, "password": customer_password}
    payload_json = json.dumps(payload_login)
    resp_login = requests.post(url=Requests.dev_api_domain+Requests.path_login, data=payload_json, headers=Requests.headers)
    print("login result:", resp_login.status_code, "/", resp_login.reason, "/", resp_login.elapsed)
    assert resp_login.status_code == 200, "status code not 200"
    assert resp_login.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_login.json()["email"] == customer_email, "email does not match"
    assert resp_login.json()['id'] != None, "required field value empty"
    assert resp_login.json()['role'] != None, "required field value empty"
    #print(resp_login.text)
    print(resp_login.json()["email"])
    global access_token
    access_token = resp_login.json()["accessToken"]
    #print(access_token)

# cd TrueQRcode/tests
# pytest test_dev_auth.py -s -vv
# pytest --count=10 test_dev_auth.py -s -vv