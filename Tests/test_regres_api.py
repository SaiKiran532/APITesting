import requests
import json
import allure

# base url:
base_url = "https://reqres.in"

# GET Request
@allure.title("Get List of Users")
@allure.description("This test case retrieves a list of users from the API.")
@allure.tag("API", "GET")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("component", "user")
@allure.link("https://reqres.in/api/users?page=2", name="List Users")
@allure.testcase("TESTCASE-1", "Test case description for Get List of Users")
@allure.epic("User Management")
@allure.feature("GET Requests")
@allure.story("Retrieve list of users")
def test_get_list_users():
    url = base_url + "/api/users?page=2"
    print("get url: " + url)
    response = requests.get(url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print(".......LIST USERS IS DONE.......")
    print(".......=====================.......")

# GET Single User
@allure.title("Get Single User")
@allure.description("This test case retrieves a single user by ID from the API.")
@allure.tag("API", "GET")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("component", "user")
@allure.link("https://reqres.in/api/users/2", name="Single User")
@allure.testcase("TESTCASE-2", "Test case description for Get Single User")
@allure.epic("User Management")
@allure.feature("GET Requests")
@allure.story("Retrieve single user by ID")
def test_get_single_user():
    url = base_url + "/api/users/2"
    print("get url: " + url)
    response = requests.get(url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print(".......LIST SINGLE USER IS DONE.......")
    print(".......=====================.......")

# GET User Not Found
@allure.title("User Not Found")
@allure.description("This test case handles the scenario where a user is not found in the API.")
@allure.tag("API", "GET")
@allure.severity(allure.severity_level.MINOR)
@allure.label("component", "user")
@allure.link("https://reqres.in/api/users/23", name="User Not Found")
@allure.testcase("TESTCASE-3", "Test case description for User Not Found")
@allure.epic("User Management")
@allure.feature("GET Requests")
@allure.story("Handle user not found")
def test_user_not_found():
    url = base_url + "/api/users/23"
    print("get url: " + url)
    response = requests.get(url)
    assert response.status_code == 404
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print(".......USER NOT FOUND.......")
    print(".......=====================.......")

# POST Request
@allure.title("Create User")
@allure.description("This test case creates a new user in the API.")
@allure.tag("API", "POST")
@allure.severity(allure.severity_level.BLOCKER)
@allure.label("component", "user")
@allure.link("https://reqres.in/api/users", name="Create User")
@allure.testcase("TESTCASE-4", "Test case description for Create User")
@allure.epic("User Management")
@allure.feature("POST Requests")
@allure.story("Create a new user")
def test_post_create_user():
    url = base_url + "/api/users"
    print("post url: " + url)

    data = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(url, json=data)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    assert response.status_code == 201
    assert "name" in json_data
    assert json_data["name"] == "morpheus"
    print(".......POST/Create USER IS DONE.......")
    print(".......=====================.......")

# UPDATE Request with PUT
@allure.title("Update User with PUT")
@allure.description("This test case updates an existing user in the API using the PUT method.")
@allure.tag("API", "PUT")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("component", "user")
@allure.link("https://reqres.in/api/users/2", name="Update User PUT")
@allure.testcase("TESTCASE-5", "Test case description for Update User with PUT")
@allure.epic("User Management")
@allure.feature("PUT Requests")
@allure.story("Update a user with PUT method")
def test_put_update_user():
    url = base_url + "/api/users/2"
    print("put url: " + url)

    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put(url, json=data)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body: ", json_str)
    assert response.status_code == 200
    assert "name" in json_data
    assert json_data["name"] == "morpheus"
    print(".......PUT/UPDATE USER IS DONE.......")
    print(".......=====================.......")

# UPDATE Request with PATCH
@allure.title("Update User with PATCH")
@allure.description("This test case updates an existing user in the API using the PATCH method.")
@allure.tag("API", "PATCH")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("component", "user")
@allure.link("https://reqres.in/api/users/2", name="Update User PATCH")
@allure.testcase("TESTCASE-6", "Test case description for Update User with PATCH")
@allure.epic("User Management")
@allure.feature("PATCH Requests")
@allure.story("Update a user with PATCH method")
def test_patch_update_user():
    url = base_url + "/api/users/2"
    print("patch url: " + url)

    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.patch(url, json=data)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PATCH response body: ", json_str)
    assert response.status_code == 200
    assert "name" in json_data
    assert json_data["name"] == "morpheus"
    print(".......PATCH/UPDATE USER IS DONE.......")
    print(".......=====================.......")

# DELETE Request
@allure.title("Delete User")
@allure.description("This test case deletes an existing user from the API.")
@allure.tag("API", "DELETE")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("component", "user")
@allure.link("https://reqres.in/api/users/2", name="Delete User")
@allure.testcase("TESTCASE-7", "Test case description for Delete User")
@allure.epic("User Management")
@allure.feature("DELETE Requests")
@allure.story("Delete a user")
def test_delete_user():
    url = base_url + "/api/users/2"
    print("Delete url: " + url)
    response = requests.delete(url)
    assert response.status_code == 204
    print(".......DELETED USER.......")
    print(".......=====================.......")