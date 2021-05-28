from json import loads

from django.test import TestCase
from requests import post, get

from test_values import TEST_URL, PASSWORD, USERNAME


def auth_token(username=USERNAME, password=PASSWORD):
    response = post(f"{TEST_URL}/api/account/sign_in", data={"username": username, "password": password})
    return loads(response.text)["access"]


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_login_LDAP(self):
        password = input("Password:")
        if password != "local":
            auth_token("Rachis.VA", password)

    def test_local_login(self):
        auth_token()

    def test_is_constructor(self):
        response = get(f"{TEST_URL}/api/account/is_constructor", headers={"Authorization": auth_token()})
        self.assertTrue(loads(response.text)["status"])
