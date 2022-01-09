from django.contrib import admin
from django.urls import path, include

# D.R.F Simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    # MODELS
    path(
        'user/',
        include("bookstore_users.urls")
    ),
    path(
        'book/',
        include("bookstore_inventory.urls")
    ),
    # TOKEN MANAGEMENT
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        "api/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
]
