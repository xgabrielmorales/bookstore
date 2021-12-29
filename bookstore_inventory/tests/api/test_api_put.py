# Django
from django.urls import reverse
# Django REST Framework
from rest_framework import status
# Local
from bookstore_inventory.models.book          import Book
from bookstore_inventory.tests.api.test_setup import TestSetUp

class BookPutTestCase(TestSetUp):
    def test_replace_book(self):
        new_book_data = {
            "title"     : self.faker_obj.color_name(),
            "author"    : self.faker_obj.name(),
            "editorial" : "Palabras",
            "gender"    : "Autobiograficos",
            "num_pages" : self.faker_obj.random_int(),
            "pub_date"  : self.faker_obj.date(),
        }

        response = self.client.put(
            reverse(
                "inventory:book_delete_put",
                kwargs = {"pk": self.book_saved.id}
            ),
            data = new_book_data,
            **self.HEADER
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], new_book_data["title"])
