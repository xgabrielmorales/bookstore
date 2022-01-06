from django.contrib import admin
from django.urls import path, include

# D.R.F Simplw JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include("bookstore_users.urls")),
    path('book/', include("bookstore_inventory.urls")),
    # Token Management
    path("api/token/",   TokenObtainPairView.as_view(), name = "token_obtain_pair"),
    path("api/refresh/", TokenRefreshView.as_view(),    name = "token_refresh"),
]
