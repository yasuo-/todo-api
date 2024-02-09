from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

HTTP_STATUS_OK = 200


class TestDone:
    def test_mark_task_as_done(self):
        response = client.put("/tasks/1/done")
        assert response.status_code == HTTP_STATUS_OK

    def test_mark_task_as_not_done(self):
        response = client.delete("/tasks/1/done")
        assert response.status_code == HTTP_STATUS_OK
