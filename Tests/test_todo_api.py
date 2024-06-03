import requests
import uuid  # universal unique id
import allure

ENDPOINT = "https://todo.pixegami.io"

# Base endpoint call
@allure.title("Call Base Endpoint")
@allure.description("This test calls the base endpoint and checks if the response status is 200.")
@allure.tag('api', 'base')
@allure.severity(allure.severity_level.NORMAL)
@allure.label('module', 'endpoint')
@allure.feature("Base Endpoint")
@allure.link(name="Base Endpoint Documentation", url="https://todo.pixegami.io/docs")
@allure.testcase("Test case ID: TC001")
@allure.epic("Base Operations")
def test_calling_end_point():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

# Create Task Test
@allure.title("Create Task")
@allure.description("This test creates a task and verifies if the task is created correctly.")
@allure.tag('api', 'task', 'create')
@allure.severity(allure.severity_level.BLOCKER)
@allure.label('module', 'task_management')
@allure.feature("Task Management")
@allure.link(name="Create Task Documentation", url="https://todo.pixegami.io/docs#create-task")
@allure.testcase("Test case ID: TC002")
@allure.epic("Task Operations")
def test_create_task():
    payload = payload_data()
    create_task_response = create_task(payload)

    assert create_task_response.status_code == 200
    data = create_task_response.json()

    task_id = data["task"]["task_id"]

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200

    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]
    assert get_task_data["task_id"] == data["task"]["task_id"]

# Update Task Test
@allure.title("Update Task")
@allure.description("This test updates a task and verifies if the task is updated correctly.")
@allure.tag('api', 'task', 'update')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('module', 'task_management')
@allure.feature("Task Management")
@allure.link(name="Update Task Documentation", url="https://todo.pixegami.io/docs#update-task")
@allure.testcase("Test case ID: TC003")
@allure.epic("Task Operations")
def test_update_task():
    payload = payload_data()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    new_payload = {
        "content": "Another Content",
        "user_id": payload["user_id"],
        "task_id": task_id,
        "is_done": True,
    }

    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["user_id"] == new_payload["user_id"]
    assert get_task_data["is_done"] == new_payload["is_done"]

# List of Tasks Test
@allure.title("List Tasks")
@allure.description("This test lists tasks for a user and verifies the number of tasks.")
@allure.tag('api', 'task', 'list')
@allure.severity(allure.severity_level.NORMAL)
@allure.label('module', 'task_management')
@allure.feature("Task Management")
@allure.link(name="List Tasks Documentation", url="https://todo.pixegami.io/docs#list-tasks")
@allure.testcase("Test case ID: TC004")
@allure.epic("Task Operations")
def test_list_of_tasks():
    n = 3
    payload = new_payload_data()
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    user_id = payload["user_id"]
    list_task_response = list_tasks(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()
    # print(data)

    task = data["tasks"]
    assert len(task) == n

# Delete Task Test
@allure.title("Delete Task")
@allure.description("This test deletes a task and verifies if the task is deleted correctly.")
@allure.tag('api', 'task', 'delete')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('module', 'task_management')
@allure.feature("Task Management")
@allure.link(name="Delete Task Documentation", url="https://todo.pixegami.io/docs#delete-task")
@allure.testcase("Test case ID: TC005")
@allure.epic("Task Operations")
def test_delete_tasks():
    payload = new_payload_data()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404

# Helper functions
def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")

def payload_data():
    return {
        "content": "Creating task",
        "user_id": "User001",
        "task_id": "Task002",
        "is_done": False,
    }

def new_payload_data():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    return {
        "content": content,
        "user_id": user_id,
        "is_done": False,
    }

