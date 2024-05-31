import requests
import json
import allure

# base url:
base_url = "https://reqres.in"


# GET Request
@allure.title("Get List of Users")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://reqres.in/api/users?page=2", name="List Users")
@allure.feature("GET Requests")
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

@allure.title("Get Single User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://reqres.in/api/users/2", name="Single User")
@allure.feature("GET Requests")
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

@allure.title("User Not Found")
@allure.severity(allure.severity_level.MINOR)
@allure.link("https://reqres.in/api/users/23", name="User Not Found")
@allure.feature("GET Requests")
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
@allure.severity(allure.severity_level.BLOCKER)
@allure.link("https://reqres.in/api/users", name="Create User")
@allure.feature("POST Requests")
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


# UPDATE Request
@allure.title("Update User with PUT")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://reqres.in/api/users/2", name="Update User PUT")
@allure.feature("PUT Requests")
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


# PATCH Request
@allure.title("Update User with PATCH")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://reqres.in/api/users/2", name="Update User PATCH")
@allure.feature("PATCH Requests")
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
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://reqres.in/api/users/2", name="Delete User")
@allure.feature("DELETE Requests")
def test_delete_user():
    url = base_url + "/api/users/2"
    print("Delete url: " + url)
    response = requests.delete(url)
    assert response.status_code == 204
    print(".......DELETED USER.......")
    print(".......=====================.......")

