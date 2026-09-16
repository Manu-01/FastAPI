
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


# ============================================================
# GET /list
# ============================================================

def test_home():
    response = client.get("/list")

    assert response.status_code == 200

    data = response.json()

    assert "data" in data
    assert len(data["data"]) == 2
    assert data["data"][0]["id"] == 1
    assert data["data"][0]["name"] == "John Doe"


# ============================================================
# GET /user/{id}
# ============================================================

def test_get_user_by_id():
    response = client.get("/user/10")

    assert response.status_code == 200

    data = response.json()

    assert data["isSuccess"] is True
    assert data["data"]["id"] == 10
    assert data["data"]["name"] == "John Doe"


def test_get_user_by_id_invalid():
    response = client.get("/user/abc")

    # FastAPI returns 422 when an int path parameter
    # receives an invalid value.
    assert response.status_code == 422


# ============================================================
# GET /user - Query Parameters
# ============================================================

def test_get_user_without_query_parameter():
    response = client.get("/user")

    assert response.status_code == 200

    data = response.json()

    assert data["isSuccess"] is True
    assert data["page"] == 0
    assert data["size"] == 10
    assert data["total"] == 2


def test_get_user_by_name():
    response = client.get(
        "/user",
        params={"name": "John"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["isSuccess"] is True
    assert data["total"] == 1
    assert data["data"][0]["name"] == "John Doe"


def test_get_user_by_email():
    response = client.get(
        "/user",
        params={"email": "awd@example.com"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["isSuccess"] is True
    assert data["total"] == 1
    assert data["data"][0]["email"] == "awd@example.com"


def test_get_user_not_found():
    response = client.get(
        "/user",
        params={"name": "Unknown"}
    )

    assert response.status_code == 200
    assert response.json() == []


def test_get_user_pagination():
    response = client.get(
        "/user",
        params={
            "page": 0,
            "size": 1
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["isSuccess"] is True
    assert data["page"] == 0
    assert data["size"] == 1
    assert data["total"] == 1
    assert len(data["data"]) == 1


# ============================================================
# POST /create-user
# ============================================================

def test_create_user():
    payload = {
        "name": "Alice",
        "email": "alice@example.com",
        "age": 25,
        "address": {
            "line1": "123 Main Road",
            "street": "MG Road",
            "city": "Delhi",
            "state": "Delhi",
            "zip_code": "110001"
        }
    }

    response = client.post(
        "/create-user",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["isSuccess"] is True
    assert data["message"] == "User created successfully"

    assert data["data"]["name"] == "Alice"
    assert data["data"]["email"] == "alice@example.com"
    assert data["data"]["age"] == 25

    assert data["data"]["address"]["city"] == "Delhi"
    assert data["data"]["address"]["zip_code"] == "110001"


# ============================================================
# POST /save-user
# ============================================================

def test_save_user():
    payload = {
        "name": "Bob",
        "email": "bob@example.com",
        "age": 30,
        "address": {
            "line1": "456 Park Street",
            "street": "Park Street",
            "city": "Mumbai",
            "state": "Maharashtra",
            "zip_code": "400001"
        }
    }

    response = client.post(
        "/save-user",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["isSuccess"] is True
    assert data["message"] == "User saved successfully"

    assert data["data"]["name"] == "Bob"
    assert data["data"]["email"] == "bob@example.com"


# ============================================================
# POST validation tests
# ============================================================

def test_create_user_missing_name():
    payload = {
        "email": "alice@example.com",
        "age": 25,
        "address": {
            "line1": "123 Main Road",
            "street": "MG Road",
            "city": "Delhi",
            "state": "Delhi",
            "zip_code": "110001"
        }
    }

    response = client.post(
        "/create-user",
        json=payload
    )

    assert response.status_code == 422


def test_create_user_missing_address():
    payload = {
        "name": "Alice",
        "email": "alice@example.com",
        "age": 25
    }

    response = client.post(
        "/create-user",
        json=payload
    )

    assert response.status_code == 422


def test_create_user_invalid_age():
    payload = {
        "name": "Alice",
        "email": "alice@example.com",
        "age": "twenty-five",
        "address": {
            "line1": "123 Main Road",
            "street": "MG Road",
            "city": "Delhi",
            "state": "Delhi",
            "zip_code": "110001"
        }
    }

    response = client.post(
        "/create-user",
        json=payload
    )

    assert response.status_code == 422
