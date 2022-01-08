# Django
from django.urls import path
# Local
from . import views
from .views import api as api_views

app_name = "inventory"

urlpatterns = [
    path(
        '',
        views.list_create_view,
        name="list_create"
    ),
    path(
        'delete/<int:pk>',
        views.delete_view,
        name="delete"
    ),
    path(
        'update/<int:pk>',
        views.update_view,
        name="update"
    ),
    # API Views
    path(
        'api/',
        api_views.BookListCreateView.as_view(),
        name="book_get_post"
    ),
    path(
        'api/<int:pk>/',
        api_views.BookDestroyUpdateView.as_view(),
        name="book_delete_put"
    ),
]
