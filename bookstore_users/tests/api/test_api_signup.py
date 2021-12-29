# Django REST Framework
from rest_framework import status
# Local
from bookstore_users.tests.api import TestSetUp
from bookstore_users.models.user import User

class UserSignUpTestCase(TestSetUp):
    def test_if_data_is_valid_then_signup(self):
        user_valid_data = {
            "first_name" : self.user_object.first_name,
            "last_name"  : self.user_object.last_name,
            "email"      : self.user_object.email,
            "password"   : self.user_object.password,
        }

        response = self.client.post(self.crear_listar_url, data = user_valid_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

        new_user = User.objects.get(email = user_valid_data["email"])
        self.assertEqual(new_user.email, self.user_object.email)

        # Password should be hashed
        user = User.objects.get(pk = self.user_saved.id)
        self.assertNotEqual(user_valid_data["password"], user.password)

    def test_user_cannot_register_with_invalid_data(self):
        user_invalid_data = {
            "invalid_first_name" : self.faker_obj.first_name(),
            "invalid_last_name"  : self.faker_obj.last_name(),
            "invalid_email"      : self.faker_obj.email(),
            "invalid_password"   : self.faker_obj.password(),
        }

        response = self.client.post(self.crear_listar_url, data = user_invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_user_cannot_regiser_with_incomplete_data(self):
        user_incomplete_data = {
            "first_name"   : self.faker_obj.first_name(),
            "password" : self.faker_obj.password(),
        }

        response = self.client.post(self.crear_listar_url, data = user_incomplete_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_user_cannot_register_with_no_data(self):
        response = self.client.post(self.crear_listar_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_if_email_already_exists_dont_signup(self):
        user_valid_data_but_with_existing_email = {
            "first_name"   : self.faker_obj.first_name(),
            "last_name" : self.faker_obj.last_name(),
            "email"    : self.user_saved.email,
            "password" : self.faker_obj.password(),
        }

        response = self.client.post(
            self.crear_listar_url,
            data = user_valid_data_but_with_existing_email
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
