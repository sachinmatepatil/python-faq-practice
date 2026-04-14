import requests
import pytest
from jsonschema import validate, ValidationError

@pytest.fixture(scope="module")
def base_url():
    return "https://api.escuelajs.co/api"

CREATE_USER_SCHEMA = {
    "type": "object",
    "required": ["name", "email", "password", "avatar"],
    "properties": {
        "name":      {"type": "string"},
        "email":       {"type": "string"},
        "password":        {"type": "string"},
        "avatar": {"type": "string"}
    }
}

def test_create_user_schema(base_url):
    payload = {"name": "Alice", "email": "alice@gmail.com", "password": "password123", "avatar": "https://example.com/avatar.jpg"}
    response = requests.post(f"{base_url}/v1/users", json=payload)

    assert response.status_code == 201
    try:
        validate(instance=response.json(), schema=CREATE_USER_SCHEMA)
    except ValidationError as e:
        pytest.fail(f"Schema validation failed: {e.message}")