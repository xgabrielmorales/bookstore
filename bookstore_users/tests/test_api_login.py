# Django REST Framework
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
# Local
from bookstore_users.tests import TestSetUp

class UserLogInTestCase(TestSetUp):
    def test_valid_login(self):
        user_data = {
            "email"   : self.user_saved.email,
            "password": self.user_saved_password,
        }

        response = self.client.post(self.login_url, data = user_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access"  in response.data)
        self.assertTrue("refresh" in response.data)

    def test_if_password_incorrect_then_cant_login(self):
        user_data = {
            "email"   : self.user_saved.email,
            "password": self.faker_obj.password(),
        }
        response = self.client.post(self.login_url, data = user_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        valid_error = {
            'detail': ErrorDetail(
                string = 'No active account found with the given credentials',
                code   = 'no_active_account'
            )
        }

        self.assertEqual(response.data, valid_error)

    def test_if_user_not_register_then_cant_login(self):
        user_data = {
            "email"    : self.faker_obj.email(),
            "password" : self.faker_obj.password(),
        }

        response = self.client.post(self.login_url, data = user_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        valid_error = {
            'detail': ErrorDetail(
                string = 'No active account found with the given credentials',
                code   = 'no_active_account'
            )
        }

        self.assertEqual(response.data, valid_error)
