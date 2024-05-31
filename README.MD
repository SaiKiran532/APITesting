# Task Management API Tests

This repository contains automated tests for the Task Management API at `https://todo.pixegami.io`. The tests are written in Python using the `requests` library for HTTP requests and `pytest` for test execution. Allure is used for test reporting.

## Endpoints

The following endpoints are tested:

- `GET /` - Base endpoint to check server status
- `PUT /create-task` - Create a new task
- `GET /get-task/{task_id}` - Retrieve a specific task by ID
- `GET /list-tasks/{user_id}` - List all tasks for a specific user
- `PUT /update-task` - Update an existing task
- `DELETE /delete-task/{task_id}` - Delete a task by ID

## Tests

The following tests are included:

- **Base Endpoint**
  - `test_calling_end_point`: Checks if the base endpoint is reachable.

- **Task Management**
  - `test_create_task`: Tests task creation and verifies the created task.
  - `test_update_task`: Tests task update functionality and verifies the updated task.
  - `test_list_of_tasks`: Tests listing tasks for a user and verifies the number of tasks.
  - `test_delete_tasks`: Tests task deletion and verifies the task is deleted.

## Test Execution

To execute the tests, follow these steps:

1. **Clone the repository:**
   ```command promt
   > git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install the required dependencies:**
   ```command promt
   > pip install requests pytest allure-pytest
   ```
3. **Run the tests using pytest:**
   ```command promt
   > pytest
   ```
