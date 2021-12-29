# Django
from django.urls import reverse
# Django REST framework
from rest_framework.test import APITestCase, APIClient
# Faker
from faker import Faker
# Local
from bookstore_inventory.tests.api.factory import BookFactory

class TestSetUp(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.book_saved  = BookFactory.create()
        cls.book_object = BookFactory.build()

        cls.faker_obj   = Faker()
        cls.client      = APIClient()
