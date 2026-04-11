# Task: Create a session fixture (module scope) that logs in, stores the auth token in the session headers,
# and yields the session. Write two tests that use it.
from idlelib.rpc import response_queue

# import requests
# import pytest
#
# @pytest.fixture(scope="module")
# def base_url():
#     return "https://restful-booker.herokuapp.com"
#
# @pytest.fixture(scope="module")
# def api_session(base_url):
#     session = requests.Session()
#
#     login_url = f"{base_url}/auth"
#     payload = {"username":"admin","password":"password123"}
#
#     response = session.post(login_url, json=payload)
#     assert response.status_code == 200, "login failed"
#     token = response.json().get("token")
#     assert token is not None, "token not found"
#
#     session.headers.update({"Cookie":f"token{token}","Content-type":"application/json"})
#     yield session
#     session.close()
#
#
# def test_get_booking_list(base_url, api_session):
#     response = api_session.get(f"{base_url}/booking")
#     assert response.status_code == 200
#
#     data = response.json()
#     assert isinstance(data, list), "get booking list failed"
#     assert "bookingid" in data[0], "bookingid not found in response"


import requests
import pytest

@pytest.fixture(scope="module")
def base_url():
    return "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="module")
def api_session(base_url):
    session = requests.Session()

    login_url = f"{base_url}/auth"
    payload = {"username":"admin","password":"password123"}

    response = session.post(login_url, json=payload)
    assert response.status_code == 200, "login failed"
    token = response.json().get("token")
    assert token is not None, "token not found"
    session.headers.update({"Cookie":f"bearer{token}", "Content-type":"application/json"})
    yield session
    session.close()

def test_get_booking_list(base_url, api_session):
    response = api_session.get(f"{base_url}/booking")
    assert response.status_code == 200, "get booking list failed"

    data = response.json()
    assert isinstance(data, list), "response is not a list"
    assert "bookingid" in data[0], "Booking ID not found in response"

def test_create_booking(base_url, api_session):
    payload = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-10"
        },
        "additionalneeds": "Breakfast"
    }
    response = api_session.post(f"{base_url}/booking", json=payload)
    assert response.status_code == 200, "Booking creation failed"

    data = response.json()
    assert "bookingid" in data, "Firstname not found in response"

    """
    ✅ session = requests.Session() — Short Explanation

It creates a persistent HTTP session.

👉 Meaning:
	•	Reuses the same connection
	•	Keeps headers, cookies, auth across multiple requests

⸻

🔥 Why we use it:
	•	Faster (no new connection each time)
	•	Maintains login state (token/cookie)
	•	Cleaner code (no need to pass headers every time)

⸻

💬 One-line interview answer:

“requests.Session() allows me to reuse connections and maintain headers/cookies across API calls, improving performance and enabling stateful testing.”
    """