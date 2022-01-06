# Django
from django.urls import path
# Local
from . import views
from .views import api

app_name = "inventory"

urlpatterns = [
    path(
        '',
        views.list_create_view,
        name="list_create"
    ),
    path(
        'api/',
        api.BookListCreateView.as_view(),
        name="book_get_post"
    ),
    path(
        'api/<int:pk>/',
        api.BookDestroyUpdateView.as_view(),
        name="book_delete_put"
    ),
]
