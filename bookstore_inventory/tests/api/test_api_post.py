# Django
from django.urls import reverse
# Django REST Framework
from rest_framework import status
# Local
from bookstore_inventory.models.book          import Book
from bookstore_inventory.tests.api.test_setup import TestSetUp

class BookPostTestCase(TestSetUp):
    def test_if_data_is_valid_create_book(self):
        valid_book_data = {
            "title"     : self.book_saved.title,
            "author"    : self.book_saved.author,
            "editorial" : self.book_saved.gender,
            "gender"    : self.book_saved.gender,
            "num_pages" : self.book_saved.num_pages,
            "pub_date"  : self.book_saved.pub_date,
        }

        response = self.client.post(
            reverse("inventory:book_get_post"),
            data = valid_book_data,
            **self.HEADER
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], valid_book_data["title"])
        self.assertEqual(Book.objects.count(), 2)

    def test_if_data_is_invalid_cant_create_book(self):
        invalid_book_data = {
            "invalid_title"     : "fake_data",
            "invalid_author"    : "fake_data",
            "invalid_editorial" : "fake_data",
        }

        response = self.client.post(
            reverse("inventory:book_get_post"),
            data = invalid_book_data,
            **self.HEADER
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.count(), 1)
