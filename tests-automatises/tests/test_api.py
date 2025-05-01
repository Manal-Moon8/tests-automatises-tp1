import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# --- Calculator endpoints ---

def test_add_api(client):
    response = client.get("/api/add/2/3")
    assert response.status_code == 200
    assert response.get_json()["result"] == 5.0

def test_divide_by_zero_api(client):
    response = client.get("/api/divide/4/0")
    assert response.status_code == 400

# --- User endpoints ---

def test_create_user_api(client):
    response = client.post("/api/user", json={
        "username": "apiuser",
        "email": "api@example.com"
    })
    assert response.status_code == 201
    assert response.get_json()["message"] == "User created successfully"

def test_get_user_api(client):
    client.post("/api/user", json={
        "username": "apiuser2",
        "email": "api2@example.com"
    })
    response = client.get("/api/user/apiuser2")
    assert response.status_code == 200
    assert response.get_json()["email"] == "api2@example.com"

def test_delete_user_api(client):
    client.post("/api/user", json={
        "username": "apidelete",
        "email": "del@example.com"
    })
    response = client.delete("/api/user/apidelete")
    assert response.status_code == 200
    assert response.get_json()["message"] == "User deleted successfully"
