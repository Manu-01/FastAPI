from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_test_api():
    response = client.get("/test/list")

    assert response.status_code == 200

    assert response.json() == {
        "data": "Test API is working fine",
        "message": "Test API is working fine",
        "isSuccess": True
    }