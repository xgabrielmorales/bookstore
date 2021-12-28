# Django
from django.urls import path
# Local
from . import views

app_name = "user"

urlpatterns = [
    path(
        '',
        views.UserCreateRetriveView.as_view(),
        name = "get_post",
    ),
    path(
        '<int:pk>/',
        views.UserDestroyUpdateView.as_view(),
        name = "delete_put",
    ),
]
