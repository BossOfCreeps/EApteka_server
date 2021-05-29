from datetime import date
from json import loads

from django.test import TestCase
from requests import post, get

from eapteka.settings import TEST_URL


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_create_notification(self):
        data = {
            "product": "8",
            "date_start": "2021-05-29",
            "times": ["10:00:00", "8:00:00"]
        }
        response = post(f"{TEST_URL}api/notification/create_notification", data=data)
        self.assertEqual(response.status_code, 200)
