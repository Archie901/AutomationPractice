import requests
import pytest
from data import Requests
from fixtures import login

def test_profile1(login):
    resp_profile = requests.get(url=Requests.dev_api_domain+Requests.path_profile, headers=pytest.headersToken)
    #print(resp_profile.text)
    print("profile request:", resp_profile.status_code, "/", resp_profile.reason, "/", resp_profile.elapsed)
    print("email from profile response:", f"-- {resp_profile.json()['email']} --")
    assert resp_profile.status_code == 200, "status code not 200"
    assert resp_profile.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_profile.json()['email'] == pytest.user_email, "email does not match"
    assert resp_profile.json()['id'] == pytest.user_id, "id does not match"
    assert resp_profile.json()['role'] == "ROLE_CUSTOMER", "role not customer"
    assert resp_profile.json()['status'] == "ACTIVE", "status not active"
    
def test_profile2(login):
    resp_profile = requests.get(url=Requests.dev_api_domain+Requests.path_profile, headers=pytest.headersToken)
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
# pytest -s -vv test_dev_profile.py
# pytest -s -vv --setup-show test_dev_profile.py
# pytest -s -vv --count=5 test_dev_profile.py