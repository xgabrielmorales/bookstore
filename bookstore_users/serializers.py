from rest_framework.serializers import ModelSerializer

from .models.user import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = [ "id", "email", "password", "nombre", "apellido", ]
        extra_kwargs = { "password": {"write_only": True} }
