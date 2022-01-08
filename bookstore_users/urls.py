# Django
from django.urls import path
# Local
from . import views

app_name = "users"

urlpatterns = [
    # API VIEWS
    path(
        'api/',
        views.UserCreateRetriveView.as_view(),
        name="get_post",
    ),
    path(
        'api/<int:pk>/',
        views.UserDestroyUpdateView.as_view(),
        name="delete_put",
    ),
]
