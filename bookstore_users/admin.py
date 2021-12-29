from django.contrib import admin

from .models import User

class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Nombres",      {"fields": ["first_name", "last_name"]}),
        ("Credenciales", {"fields": ["email", "password"]}),
        ("Atributos",    {"fields": ["is_active", "is_staff", "is_superuser"]}),
        ("Otros",        {"fields": ["last_login"]})
    ]

    search_fields = ['first_name', "last_name"]
    list_display = ("__str__", "email")

admin.site.register(User, UsuarioAdmin)
