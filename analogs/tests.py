from datetime import date
from json import loads

from django.test import TestCase
from requests import post, get

from eapteka.settings import TEST_URL


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_create_analogs(self):
        data = {
            'products': [
                """{
                    'product': 1,
                    'number_of_times': 5,
                    'reception_time': 'before_eating',
                    'pieces_at_time': 1,
                    'date_start': date(day=29, month=5, year=2021),
                    'date_end': date(day=31, month=5, year=2021),
                    'text': 'comment'
                }""",
            ]
        }
        response = post(f"{TEST_URL}api/analogs/add", data=data)
