

# Task: Use the requests library to call GET /api/users. Assert status is 200,
# Content-Type is JSON, and the response body is a list with at least one item.

import requests
import pytest

@pytest.fixture()
def base_url():
    return "https://jsonplaceholder.typicode.com/"


def test_get_users_returns_list(base_url):
    response = requests.get(f"{base_url}/users", params={"page": 1})
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0
    user = body[0]
    assert "id" in user
    assert "email" in user


