# Django
from django.urls import path
# Local
from . import views
from .views import api

app_name = "inventory"

urlpatterns = [
    path(
        '',
        api.BookListCreateView.as_view(),
        name="book_get_post"
    ),
    path(
        '<int:pk>/',
        api.BookDestroyUpdateView.as_view(),
        name="book_delete_put"
    ),
]
