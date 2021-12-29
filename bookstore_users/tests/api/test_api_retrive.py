# Django REST Framework
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
# Local
from bookstore_users.tests.api import TestSetUp

class UserRetriveTestCase(TestSetUp):
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

    def test_retrive_user_data(self):

        response = self.client.get(self.crear_listar_url, **self.HEADER)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user_saved.email)

    def test_user_cannot_retrive_data_from_another_user(self):
        pass
    def test_user_cannot_retrive_their_data_with_invalid_token(self):
        invalid_token = "xxxxxxAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."          + \
            "eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQwNTI1OTEzLCJ"    + \
            "pYXQiOjE2NDA1MjU2MTMsImp0aSI6IjZxxxxxxxxxxxxxxxQxYTA4NzM5N" + \
            "WUxYjljY2RjOWJkIixxxxxxxxxxZCI6MX0.gSU-Ip88k9Ike0ldbsz2sZS" + \
            "H87yU7OjMagORXLIARD8"

        HEADER = {"HTTP_AUTHORIZATION": f"Bearer {invalid_token}"}

        response = self.client.get(self.crear_listar_url, **HEADER)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        valid_errors = {
            'detail': ErrorDetail(
                string = 'Given token not valid for any token type', code = 'token_not_valid'),
            'code': ErrorDetail(
                string = 'token_not_valid', code = 'token_not_valid'
            ),
        }

        self.assertEqual(response.data["detail"], valid_errors["detail"])
        self.assertEqual(response.data["code"], valid_errors["code"])

    def test_user_cannot_retrive_his_data_without_token(self):
        HEADER = {}
        response = self.client.get(self.crear_listar_url, **HEADER)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

