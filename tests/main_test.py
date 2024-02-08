from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestMain:
    def test_read_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

    def test_read_say_hello(self):
        response = client.get("/hello/john")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello john"}
