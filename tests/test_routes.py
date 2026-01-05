import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username":"testuser","password":"testpass"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_create_item():
    response = client.post("/items/", json={"title":"Test Item","description":"Test desc"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Item"

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
