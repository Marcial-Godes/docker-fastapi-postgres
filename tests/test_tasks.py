def test_root(client):
    res = client.get("/")
    assert res.status_code == 200


def test_create_task(client):
    res = client.post("/tasks", json={"title": "Test", "completed": False})
    assert res.status_code == 201
    data = res.json()
    assert data["title"] == "Test"


def test_get_tasks(client):
    res = client.get("/tasks")
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_update_task(client):
    res = client.post("/tasks", json={"title": "Task", "completed": False})
    task_id = res.json()["id"]

    res = client.put(f"/tasks/{task_id}", json={"title": "Updated", "completed": True})
    assert res.status_code == 200
    data = res.json()
    assert data["title"] == "Updated"
    assert data["completed"] is True


def test_delete_task(client):
    res = client.post("/tasks", json={"title": "Delete", "completed": False})
    task_id = res.json()["id"]

    res = client.delete(f"/tasks/{task_id}")
    assert res.status_code == 204

    res = client.get(f"/tasks/{task_id}")
    assert res.status_code == 404
