
def test_register_user(client):
    data = {
        "username": "miriam",
        "password": "123456",
        "email": "miriam@example.com"
    }

    res = client.post("/register", json=data)

    assert res.status_code == 200
    assert res.json()["username"] == "miriam"
