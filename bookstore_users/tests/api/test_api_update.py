from django.urls import reverse
# Django REST Framework
from rest_framework import status
# Local
from bookstore_users.tests.api import TestSetUp

class UserUpdateTestCase(TestSetUp):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        user_data = {
            "email"    : cls.user_saved.email,
            "password" : cls.raw_password,
        }

        response   = cls.client.post(cls.login_url, user_data)
        cls.token  = response.data["access"]
        cls.HEADER = {"HTTP_AUTHORIZATION": f"Bearer {cls.token}"}

    def test_user_update_all_their_data(self):
        new_user_data = {
            "first_name"   : self.faker_obj.first_name(),
            "last_name" : self.faker_obj.last_name(),
            "email"    : self.faker_obj.email(),
            "password" : self.faker_obj.password(),
        }

        response = self.client.put(
            reverse(
                "users:delete_put",
                kwargs = {"pk": self.user_saved.id}
            ),
            data = new_user_data,
            **self.HEADER,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_user_data["email"], response.data["email"])
        self.assertEqual(new_user_data["first_name"], response.data["first_name"])

    def test_user_cant_update_data_of_another_user(self):
        new_user_data = {
            "first_name"   : self.faker_obj.first_name(),
            "last_name" : self.faker_obj.last_name(),
            "email"    : self.faker_obj.email(),
            "password" : self.faker_obj.password(),
        }

        response = self.client.put(
            reverse(
                "users:delete_put",
                kwargs = {"pk": self.user_saved.id + 5}
            ),
            data = new_user_data,
            **self.HEADER,
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_cant_update_their_data_if_isnt_logged_in(self):
        new_user_data = {
            "first_name"   : self.faker_obj.first_name(),
            "last_name" : self.faker_obj.last_name(),
            "email"    : self.faker_obj.email(),
            "password" : self.faker_obj.password(),
        }

        response = self.client.put(
            reverse(
                "users:delete_put",
                kwargs = {"pk": self.user_saved.id + 5}
            ),
            data = new_user_data,
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
