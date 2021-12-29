# Django
from django.urls import reverse
# Django REST Framework
from rest_framework import status
# Local
from bookstore_inventory.models.book          import Book
from bookstore_inventory.tests.api.test_setup import TestSetUp

class BookGetTestCase(TestSetUp):
    def test_list_all_books(self):
        response = self.client.get(reverse("inventory:book_get_post"), **self.HEADER)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
