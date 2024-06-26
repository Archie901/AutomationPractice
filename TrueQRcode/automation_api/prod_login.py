import requests
import json
import _main
import adata as ad

def login():
    customer_email = ad.Creds.prod_customerCreds[0]
    #customer_email = 'loscut@mailinator.com'
    customer_password = ad.Creds.prod_customerCreds[1]
    #customer_password = 'Qwerty123!'
    payload_login = {"authType": "TOKEN", "email": customer_email, "password": customer_password}
    payload_json = json.dumps(payload_login)
    resp_login = requests.post(url=ad.Requests.prod_api_domain+ad.Requests.path_login,
                               data=payload_json, headers=ad.Requests.headers)
    print(resp_login.text)
    print("login request:", resp_login.status_code, "/", resp_login.elapsed)
    print("email from login response:", f"-- {resp_login.json()["email"]} --")
    assert resp_login.status_code == 200, "status code not 200"
    assert resp_login.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_login.json()["email"] == customer_email, "email does not match"
    assert resp_login.json()['id'] != None, "required field value empty"
    assert resp_login.json()['role'] != None, "required field value empty"
    global access_token
    access_token = resp_login.json()["accessToken"]
    print(access_token)
    
login()