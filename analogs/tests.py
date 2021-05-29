from datetime import date
from json import loads

from django.test import TestCase
from requests import post, get

from eapteka.settings import TEST_URL


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_add_analog_set(self):
        data = {
            "products": ["1"],
            "number_of_times": "5",
            "days": "4",
            "reception_method": "1",
            "reception_time": "before_eating",
            "dosage": "209",
            "text": "text",
        }
        response = post(f"{TEST_URL}api/analogs/add", data=data)
        self.assertEqual(response.status_code, 200)
