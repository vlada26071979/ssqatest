import time
import pytest
import random
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password
from ssqatest.api.client import ApiClient
from ssqatest.src.helpers.assertions import Ensure

BASE_URL = "https://fakestoreapi.com"
ensure = Ensure()


@pytest.fixture(scope="module")
def api():
    return ApiClient(BASE_URL)


@pytest.mark.tcid100
def test_get_all_products(api):
    endpoint = "/products"
    response = api.get(endpoint)
    print(response.status_code)
    ensure.is_equal(response.status_code, 200)

    all_products = response.json()
    for product in all_products:
        print(f"Product id: {product['id']}")
        print(f"Product name: {product['title']}")


@pytest.mark.tcid101
def test_get_all_registered_users(api):
    endpoint = "/users"
    response = api.get(endpoint)
    print(response.status_code)
    ensure.is_equal(response.status_code, 200)

    all_registered_users = response.json()
    print(f"There are total of {len(all_registered_users)} registered users")
    print(all_registered_users[0])

    for user in all_registered_users:
        ensure.is_not_none(user["id"])


@pytest.mark.tcid102
def test_add_new_user(api):
    endpoint = "/users"

    email, password = generate_random_email_and_password()

    payload = {
        "username": f"test_user_{random.randint(1000, 9999)}",
        "email": email,
        "password": password
    }

    response = api.post(endpoint, json=payload)
    print(f"\nResponse code is {response.status_code}")
    ensure.is_equal(response.status_code, 201)

    json_response = response.json()
    print(json_response)
    ensure.is_not_none(json_response["id"])
    print(f"User is successfully created with id {json_response['id']}")



