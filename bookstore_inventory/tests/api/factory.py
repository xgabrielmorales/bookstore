from factory import Faker, django
from faker   import Faker as FakerClass

from bookstore_inventory.models.book import Book

class BookFactory(django.DjangoModelFactory):
    class Meta:
        model = Book

    title     = Faker("color_name")
    author    = Faker("name")
    editorial = "Papel"
    gender    = "Poesía"
    num_pages = Faker("random_int")
    pub_date  = Faker("date")

