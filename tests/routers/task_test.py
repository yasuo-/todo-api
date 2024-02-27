from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

HTTP_STATUS_OK = 200
TASK_DATA = {"id": 1, "title": "Task 1", "done": False}
BODY_DATA = {"title": "data"}
CREATED_TASK = {"id": 1, "title": "data", "done": False}
TASK_LENGTH = 2


class TestTask:
    def test_read_tasks(self):
        response = client.get("/tasks")
        assert response.status_code == HTTP_STATUS_OK
        assert len(response.json()) == TASK_LENGTH

    def test_create_task(self):
        response = client.post("/tasks", json=BODY_DATA)
        assert response.status_code == HTTP_STATUS_OK
        assert response.json() == CREATED_TASK

    def test_read_task(self):
        response = client.get("/tasks/1")
        assert response.status_code == HTTP_STATUS_OK
        assert response.json() == TASK_DATA

    def test_update_task(self):
        response = client.put("/tasks/1", json=BODY_DATA)
        assert response.status_code == HTTP_STATUS_OK
        assert response.json() == CREATED_TASK

    def test_delete_task(self):
        response = client.delete("/tasks/1")
        assert response.status_code == HTTP_STATUS_OK
