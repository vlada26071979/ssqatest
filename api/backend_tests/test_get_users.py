import time

import pytest
from ssqatest.api.client import ApiClient
from ssqatest.src.helpers.assertions import Ensure

BASE_URL = "https://reqres.in/api"
ensure = Ensure()


@pytest.fixture(scope="module")
def api():
    return ApiClient(BASE_URL)


@pytest.mark.tcid100
def test_all_users_have_id(api):
    response = api.get("/users")
    print(response.status_code)
    time.sleep(3)
    ensure.is_equal(response.status_code, 200)
    json_response = response.json()

    data = json_response["data"]

    for user in data:
        print(user["id"])
        print(user["email"])
        print("========================")
