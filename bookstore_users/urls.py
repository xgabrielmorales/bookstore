# Django
from django.urls import path
# Local
from . import views
from .views import api as api_views

app_name = "users"

urlpatterns = [
    path(
        'login/',
        views.login_view,
        name="login"
    ),
    # API VIEWS
    path(
        'api/',
        api_views.UserCreateRetriveView.as_view(),
        name="get_post",
    ),
    path(
        'api/<int:pk>/',
        api_views.UserDestroyUpdateView.as_view(),
        name="delete_put",
    ),
]
