from rest_framework.serializers import ModelSerializer

from .models.user import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [ "id", "email", "password", "first_name", "last_name", ]
        extra_kwargs = { "password": {"write_only": True} }
