from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

HTTP_STATUS_OK = 200


class TestTask:
    def test_read_tasks(self):
        response = client.get("/tasks")
        assert response.status_code == HTTP_STATUS_OK

    def test_create_task(self):
        response = client.post("/tasks", json={"body": "data"})
        assert response.status_code == HTTP_STATUS_OK

    def test_read_task(self):
        response = client.get("/tasks/1")
        assert response.status_code == HTTP_STATUS_OK

    def test_update_task(self):
        response = client.put("/tasks/1", json={"body": "data"})
        assert response.status_code == HTTP_STATUS_OK

    def test_delete_task(self):
        response = client.delete("/tasks/1")
        assert response.status_code == HTTP_STATUS_OK
