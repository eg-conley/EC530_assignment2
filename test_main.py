# structure created with ChatGPT, will add extra tests
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_house():
    response = client.post("/house/", params={
        "house_id": 1,
        "name": "My House",
        "address": "123 Street",
    }, json={
        "gps": [50.123, -122.456],
        "owner": {"username": "test_user"},
        "occupants": [{"username": "Alice"}, {"username": "Bob"}]
    })
    assert response.status_code == 200
    assert response.json()["message"] == "House created successfully"

def test_create_user():
    response = client.post("/user/", params={
        "user_id": 1,
        "username": "test_user",
        "phone": "1234567890",
        "email": "test@example.com"
    })
    print(response.json())  # Print the response for debugging

    assert response.status_code == 200
    assert response.json()["message"] == "User created successfully"

def test_get_nonexistent_user():
    response = client.get("/user/999")  # User ID that doesn't exist
    assert response.status_code == 200
    assert "error" in response.json()

