import requests
import json
import pytest
import _main
import adata as ad

@pytest.mark.parametrize(
        "email, password", [
            [ad.Creds.dev_customerCreds[7][0], ad.Creds.dev_customerCreds[7][1]],
            [ad.Creds.dev_customerCreds[8][0], ad.Creds.dev_customerCreds[8][1]],
            [ad.Creds.dev_customerCreds[9][0], ad.Creds.dev_customerCreds[9][1]]
        ],
    )
def test_login_profile1(email, password):
    customer_email = email
    customer_password = password
    payload_login = {"authType": "TOKEN", "email": customer_email, "password": customer_password}
    payload_json = json.dumps(payload_login)
    resp_login = requests.post(url=ad.Requests.dev_api_domain+ad.Requests.path_login,
                               data=payload_json, headers=ad.Requests.headers)
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
    resp_profile = requests.get(url=ad.Requests.dev_api_domain+ad.Requests.path_profile,
                                headers=pytest.headersToken)
    #print(resp_profile.text)
    print("profile request:", resp_profile.status_code, "/", resp_profile.reason, "/", resp_profile.elapsed)
    print("email from profile response:", f"-- {resp_profile.json()['email']} --")
    assert resp_profile.status_code == 200, "status code not 200"
    assert resp_profile.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_profile.json()['email'] == pytest.user_email, "email does not match"
    assert resp_profile.json()['id'] == pytest.user_id, "id does not match"
    assert resp_profile.json()['role'] == "ROLE_CUSTOMER", "role not customer"
    assert resp_profile.json()['status'] == "ACTIVE", "status not active"

@pytest.mark.skip
@pytest.mark.parametrize(
        "email, password", [
            [ad.Creds.dev_customerCreds[7][0], ad.Creds.dev_customerCreds[7][1]],
            [ad.Creds.dev_customerCreds[8][0], ad.Creds.dev_customerCreds[8][1]],
            [ad.Creds.dev_customerCreds[9][0], ad.Creds.dev_customerCreds[9][1]]
        ],
    )
def test_login_profile2(email, password):
    customer_email = email
    customer_password = password
    payload_login = {"authType": "TOKEN", "email": customer_email, "password": customer_password}
    payload_json = json.dumps(payload_login)
    resp_login = requests.post(url=ad.Requests.dev_api_domain+ad.Requests.path_login,
                               data=payload_json, headers=ad.Requests.headers)
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
    resp_profile = requests.get(url=ad.Requests.dev_api_domain+ad.Requests.path_profile,
                                headers=pytest.headersToken)
    #print(resp_profile.text)
    print("profile request:", resp_profile.status_code, "/", resp_profile.reason, "/", resp_profile.elapsed)
    print("email from profile response:", f"-- {resp_profile.json()['email']} --")
    assert resp_profile.status_code == 200, "status code not 200"
    assert resp_profile.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_profile.json()['email'] == pytest.user_email, "email does not match"
    assert resp_profile.json()['id'] == pytest.user_id, "id does not match"
    assert resp_profile.json()['role'] == "ROLE_CUSTOMER", "role not customer"
    assert resp_profile.json()['status'] == "ACTIVE", "status not active"

# cd Trueqrcode/tests
# pytest -s -vv test_dev_auth.py
# pytest -s -vv --setup-show test_dev_auth.py
# pytest -s -vv --count=5 test_dev_auth.py
    
if __name__ == '__main__':
    pytest.main(["-s", "-vv", "Trueqrcode/tests/test_dev_auth.py"])