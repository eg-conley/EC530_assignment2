# structure created with ChatGPT, added extra tests
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_house():
    response = client.post("/houses/", json={
        "house_id": 1,
        "name": "My House",
        "address": "123 Street",
        "gps": {"latitude": 50.123,
                "longitude": -122.456
                }
    })
    assert response.status_code == 200
    assert response.json()["message"] == "House created successfully"

def test_create_user():
    response = client.post("/users/", json={
        "user_id": 1,
        "username": "test_user",
        "phone": "1234567890",
        "email": "test@example.com"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "User created successfully"

def test_get_nonexistent_user():
    response = client.get("/users/999")  # User ID that doesn't exist
    assert response.status_code == 200
    assert "Error" in response.json()

