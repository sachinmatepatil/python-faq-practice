

import requests
import pytest

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.mark.smoke
def test_api_response(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 0.1


@pytest.mark.parametrize("id, expected_email", [(1,"Sincere@april.biz"),(2,"Shanna@melissa.tv")])
def test_users(base_url, id, expected_email):
    response = requests.get(f"{base_url}/users/{id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == id
    assert data["email"] == expected_email
    assert "email" in data
    assert "name" in data

def test_data_match():
    api_data = {'id': 1, 'name': 'Leanne Graham', 'email': 'sac@gmail.com'}
    expected_data = {'id': 1, 'name': 'Leanne Graham', 'email': 'sac@gmail.com'}

    assert api_data == expected_data, f"Data mismatch: {api_data} != {expected_data}"


def test_creation(base_url):
    payload = {
        "userId": 3,
        "id": 101,
        "title": "Test Post",
        "body": "This is a test post created for API testing."
    }
    response = requests.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]

@pytest.mark.parametrize("id",[1,2,3])
def test_validate_user(base_url,id):
    response = requests.get(f"{base_url}/users/{id}")
    assert response.status_code == 200

    data = response.json()

    assert data["id"] == id
    assert "email" in data

    assert response.elapsed.total_seconds() < 2