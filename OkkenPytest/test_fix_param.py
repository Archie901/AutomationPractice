import pytest
import json
import requests

'''@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    return request.param

def test_finish(cards_db, start_state):
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"'''

@pytest.fixture(params=(
    ["newest@mailinator.com", "Qwerty123!"],
    ["selovi@maildrop.cc", "Qwerty123!"],
    ["munic@maildrop.cc", "Qwerty123!"]
)
)
def paramers(request):
    return request.param

def test_login(paramers):
    customer_email = paramers[0]
    customer_password = paramers[1]
    payload_login = {"authType": "TOKEN", "email": customer_email, "password": customer_password}
    payload_json = json.dumps(payload_login)
    resp_login = requests.post(url='https://api-dev.trueqrcode.com/api/v1/public/auth/sign-in',
                               data=payload_json,
                               headers={"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                                        "Connection": "keep-alive"}
)
    print(resp_login.text)
    print("login request:", resp_login.status_code, "/", resp_login.reason, "/", resp_login.elapsed)
    print("email from login response:", f"-- {resp_login.json()["email"]} --")
    assert resp_login.status_code == 200, "status pytest -vv -s  test_fix_param.py  code not 200"
    assert resp_login.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_login.json()['email'] == customer_email, "email does not match"
    assert resp_login.json()['id'] != None, "required id field value empty"
    assert resp_login.json()['role'] != None, "required role field value empty"