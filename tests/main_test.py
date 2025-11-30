from fastapi.testclient import TestClient
import pytest
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_register_user(client):
    response = client.post("/register", json={
        "username": "mariam",
        "password": "mariam",
        "email": "mariam@test.com"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "mariam"


def test_login_user(client):

    client.post("/register", json={
        "username": "mariam",
        "password": "mariam",
        "email": "mariam@test.com"
    })

    response = client.post("/login", json={
        "username": "mariam",
        "password": "mariam"
    })

    assert response.status_code == 200
    assert "token" in response.json()