# Django
from django.urls import path
# Local
from . import views

app_name = "inventory"

urlpatterns = [
    path(
        '',
        views.BookListCreateView.as_view(),
        name = "list_create"
    ),
    path(
        '<int:pk>/',
        views.BookDestroyUpdateView.as_view(),
        name = "destroy_update"
    ),
]
