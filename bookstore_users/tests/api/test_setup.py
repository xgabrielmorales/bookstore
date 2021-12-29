# Django
from django.urls import reverse
# Django REST framework
from rest_framework.test import APITestCase, APIClient
# Faker
from faker import Faker
# Local
from bookstore_users.tests.api.factory import UserFactory

class TestSetUp(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user_saved = UserFactory.create()
        cls.raw_password = cls.user_saved.password
        cls.user_saved.set_password(cls.raw_password)
        cls.user_saved.save()

        cls.user_object = UserFactory.build()
        cls.faker_obj   = Faker()
        cls.client      = APIClient()

        cls.login_url   = reverse("token_obtain_pair")
        cls.refresh_url = reverse("token_refresh")
        cls.crear_listar_url = reverse("users:get_post")
