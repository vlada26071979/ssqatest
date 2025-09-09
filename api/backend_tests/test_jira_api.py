import os

import dotenv
import pytest
import requests
from requests.auth import HTTPBasicAuth
import json
from ssqatest.api.client import ApiClient
from ssqatest.src.helpers.assertions import Ensure
from dotenv import load_dotenv


BASE_URL = "https://ifeaniemeghara17.atlassian.net"
ensure = Ensure()
load_dotenv()

jira_user = os.getenv("JIRA_USER")
jira_token = os.getenv("JIRA_TOKEN")

auth = HTTPBasicAuth(jira_user, jira_token)


headers = {
    "Accept": "application/json"
}


@pytest.fixture(scope="module")
def api():
    return ApiClient(BASE_URL)


@pytest.mark.tcid103
def test_get_all_projects(api):
    endpoint = "/rest/api/3/project/search"
    response = api.get(endpoint, auth=auth, headers=headers)
    print(f"\nResponse code is {response.status_code}")
    ensure.is_equal(response.status_code, 200)

    json_response = response.json()
    print(json_response)


@pytest.mark.tcid104
def test_get_account_info(api):
    endpoint = "/rest/api/3/user"
    query = {
        "accountId": "62d684cd9189e98a20187a30"
    }
    response = api.get(endpoint, auth=auth, headers=headers, params=query)
    print(f"\nResponse code is {response.status_code}")
    ensure.is_equal(response.status_code, 200)

    json_response = response.json()
    ensure.is_equal(json_response["displayName"], "Vladimir Djordjevic")
    ensure.is_equal(json_response["emailAddress"], "ifeani.emeghara17@gmail.com")
    ensure.is_equal(json_response["active"], True)
