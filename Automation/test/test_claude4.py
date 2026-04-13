import requests
import pytest
from jsonschema import validate, ValidationError

BASE_URL = "https://reqres.in/api"

CREATE_USER_SCHEMA = {
    "type": "object",
    "required": ["name", "job", "id", "createdAt"],
    "properties": {
        "name":      {"type": "string"},
        "job":       {"type": "string"},
        "id":        {"type": "string"},
        "createdAt": {"type": "string"}
    },
    "additionalProperties": False
}

def test_create_user_schema():
    payload = {"name": "Alice", "job": "QA Engineer"}
    response = requests.post(f"{BASE_URL}/users", json=payload)

    assert response.status_code == 201
    try:
        validate(instance=response.json(), schema=CREATE_USER_SCHEMA)
    except ValidationError as e:
        pytest.fail(f"Schema validation failed: {e.message}")