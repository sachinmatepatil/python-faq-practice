# Task: Parametrize a test with (email, password, expected_status) tuples — one valid (200), one wrong password (401),
# one bad email format (422). Assert the status code each time.

import pytest
import requests

@pytest.fixture()
def base_url():
    return "https://api.escuelajs.co/api"

@pytest.mark.parametrize('email, password, expected_status', [('john@mail.com','changeme',201),('test','password',401),('asasd@asd@com','pass',401)])
def test_login(base_url, email, password, expected_status):
    response = requests.post((f"{base_url}/v1/auth/login"), json={"email": email, "password": password})
    assert response.status_code == expected_status

