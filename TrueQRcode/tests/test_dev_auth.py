import requests
import json
from tdata import Requests, Customers, Methods

def test_login_profile():
    customer_email = Customers.dev_customerCreds[7][0]
    customer_password = Customers.dev_customerCreds[7][1]
    payload_login = {"authType": "TOKEN", "email": customer_email, "password": customer_password}
    payload_json = json.dumps(payload_login)
    resp_login = requests.post(url=Requests.dev_api_domain+Requests.path_login, data=payload_json, headers=Requests.headers)
    #print(resp_login.text)
    print("login request:", resp_login.status_code, "/", resp_login.reason, "/", resp_login.elapsed)
    print("email from login response:", f"-- {resp_login.json()["email"]} --")
    assert resp_login.status_code == 200, "status code not 200"
    assert resp_login.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_login.json()['email'] == customer_email, "email does not match"
    assert resp_login.json()['id'] != None, "required field value empty"
    assert resp_login.json()['role'] != None, "required field value empty"
    global resp_login_id, resp_login_email, access_token
    resp_login_id = resp_login.json()['id']
    resp_login_email = resp_login.json()['email']
    access_token = resp_login.json()["accessToken"]
    #print(access_token)
    
    headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                   "Connection": "keep-alive", "Authorization": "Bearer " + access_token}
    resp_profile = requests.get(url=Requests.dev_api_domain+Requests.path_profile, headers=headersToken)
    #print(resp_profile.text)
    print("profile request:", resp_profile.status_code, "/", resp_profile.reason, "/", resp_profile.elapsed)
    print("email from profile response:", f"-- {resp_profile.json()['email']} --")
    assert resp_profile.status_code == 200, "status code not 200"
    assert resp_profile.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_profile.json()['email'] == resp_login_email, "email does not match"
    assert resp_profile.json()['id'] == resp_login_id, "id does not match"
    assert resp_profile.json()['role'] == "ROLE_CUSTOMER", "role not customer"
    assert resp_profile.json()['status'] == "ACTIVE", "status not active"
    
# cd TrueQRcode/tests
# pytest test_dev_auth.py -s -vv
# pytest --count=5 test_dev_auth.py -s -vv