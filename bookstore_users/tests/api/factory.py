from faker   import Faker as FakerClass
from factory import Faker, django

from bookstore_users.models.user import User

class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = Faker("first_name")
    last_name  = Faker("last_name")
    email      = Faker("email")
    password   = FakerClass().password()
