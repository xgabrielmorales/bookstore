# Django
from django.urls import path
# Local
from . import views

app_name = "inventory"

urlpatterns = [
    path(
        '',
        views.BookListCreateView.as_view(),
        name = "book_get_post"
    ),
    path(
        '<int:pk>/',
        views.BookDestroyUpdateView.as_view(),
        name = "book_delete_put"
    ),
]
