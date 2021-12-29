from django.db import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password
from .userManager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    # "password" field is already included in AbstractBaseUser

    username = None
    email    = models.EmailField(unique = True)

    first_name = models.CharField(max_length = 80, blank = True)
    last_name  = models.CharField(max_length = 80, blank = True)

    is_superuser = models.BooleanField(default = False)
    is_staff     = models.BooleanField(default = False)
    is_active    = models.BooleanField(default = True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name}" if not self.last_name \
            else f"{self.first_name} {self.last_name}"
