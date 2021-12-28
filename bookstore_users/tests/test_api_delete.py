from django.urls import reverse
# Django REST Framework
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
# Local
from bookstore_users.tests import TestSetUp
from bookstore_users.models.user import User

class UserDeleteTestCase(TestSetUp):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        user_data = {
            "email"    : cls.user_saved.email,
            "password" : cls.user_saved_password,
        }

        response = cls.client.post(cls.login_url, user_data)

        cls.token  = response.data["access"]
        cls.HEADER = {"HTTP_AUTHORIZATION": f"Bearer {cls.token}"}

    def test_user_can_delete_their_data(self):
        response = self.client.delete(
            reverse(
                "user:delete_put",
                kwargs = {"pk": self.user_saved.id}
            ),
            **self.HEADER
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

    def test_user_cant_delete_data_of_another_user(self):
        response = self.client.delete(
            reverse(
                "user:delete_put",
                kwargs = {"pk": self.user_saved.id + 4}
            ),
            **self.HEADER
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_cant_delet_their_data_if_isnt_logged_in(self):
        valid_error = {
            'detail': ErrorDetail(
                string = 'Authentication credentials were not provided.',
                code = 'not_authenticated'
            )
        }

        response = self.client.delete(
            reverse(
                "user:delete_put",
                kwargs = {"pk": self.user_saved.id}
            ),
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, valid_error)
