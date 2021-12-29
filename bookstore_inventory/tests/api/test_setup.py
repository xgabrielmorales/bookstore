# Django
from django.urls import reverse
# Django REST framework
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# Faker
from faker import Faker
# Local
from bookstore_inventory.tests.api.factory import BookFactory
from bookstore_users.tests.api.factory import UserFactory

class TestSetUp(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.book_saved  = BookFactory.create()
        cls.book_object = BookFactory.build()

        cls.faker_obj   = Faker()
        cls.client      = APIClient()

        user_saved = UserFactory.create()
        raw_password = user_saved.password
        user_saved.set_password(raw_password)
        user_saved.save()

        user_data = {
            "email"    : user_saved.email,
            "password" : raw_password,
        }

        tokenSerializer = TokenObtainPairSerializer(data = user_data)
        tokenSerializer.is_valid()
        access_token = tokenSerializer.validated_data["access"]

        cls.HEADER = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
