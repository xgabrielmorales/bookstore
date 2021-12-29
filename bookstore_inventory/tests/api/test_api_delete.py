# Django
from django.urls import reverse
# Django REST Framework
from rest_framework import status
# Local
from bookstore_inventory.models.book          import Book
from bookstore_inventory.tests.api.test_setup import TestSetUp

class BookDeleteTestCase(TestSetUp):
    def test_delete_book(self):

        response = self.client.delete(
            reverse(
                "inventory:book_delete_put",
                kwargs = {"pk": self.book_saved.id}
            ),
            **self.HEADER
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(Book.objects.count(), 0)
