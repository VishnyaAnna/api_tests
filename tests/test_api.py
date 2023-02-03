import requests
from requests import Response
from pytest_voluptuous import S
from schemas import schemas
from schemas.schemas import base_url


def test_create_single_user():
    created_user: Response = requests.post(
        url=f"{base_url}api/users",
        json=
        {
            "name": "Anna",
            "job": "QA"
        }
    )
    assert created_user.status_code == 201
    assert created_user.json()["name"] == "Anna"
    assert S(schemas.create_single_user) == created_user.json()
    assert len(created_user.json()) == 4


def test_register_single_user():
    registered_user: Response = requests.post(
        url=f"{base_url}api/register",
        json=
        {
            "email": "eve.holt@reqres.in",
            "password": "0101"
        }
    )
    assert registered_user.status_code == 200
    assert S(schemas.register_single_user) == registered_user.json()
    assert registered_user.json()["token"] is not None


def test_update_single_user():
    create_user: Response = requests.post(
        url=f"{base_url}api/users",
        json=
        {
            "name": "Anna",
            "job": "QA"
        }
    )
    result: Response = requests.put(
        url=f"{base_url}api/users/2",
        json=
        {
            "name": "Anna_V",
            "job": "QA_engineer"
        }
    )
    assert result.status_code == 200
    assert S(schemas.update_single_user) == result.json()
    assert result.json()["job"] == "QA_engineer"
    assert result.json()["name"] == "Anna_V"


def test_login_single_user_successful():
    login_user: Response = requests.post(
        url=f"{base_url}api/login",
        json=
        {
            "email": "eve.holt@reqres.in",
            "password": "0101"
        }
    )
    assert login_user.status_code == 200
    assert S(schemas.login_single_user_successful) == login_user.json()
    assert len(login_user.json()["token"]) == 17


def test_login_user_unsuccessful():
    login_user: Response = requests.post(
        url=f"{base_url}api/login",
        json=
        {
            "email": "anna.holt@reqres.in"
        }
    )
    assert login_user.status_code == 400
    assert S(schemas.login_single_user_unsuccessful) == login_user.json()
    assert login_user.json()["error"] == "Missing password"
