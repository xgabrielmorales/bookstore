from django.contrib.auth.models  import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise Value("No es posible crear un usuario sin email")

        email = self.normalize_email(email)

        user = self.model(
            email = email,
            **extra_fields,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff",     True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active",    True)

        if extra_fields["is_staff"] == False:
            raise Value("No es posible crear un superuser sin is_staff=True")
        if extra_fields["is_superuser"] == False:
            raise Value("No es posible crear un superuser sin is_superuser=True")

        return self.create_user(email, password, **extra_fields)

