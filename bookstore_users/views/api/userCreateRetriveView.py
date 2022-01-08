# Django
from django.conf import settings
# Django REST Framework
from rest_framework.generics    import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response    import Response
from rest_framework             import status
# Django REST Framework Simple JWT
from rest_framework_simplejwt.backends    import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# Local
from bookstore_users.models.user import User
from bookstore_users.serializers import UserSerializer

class UserCreateRetriveView(GenericAPIView):
    serializer_class   = UserSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            token        = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
            tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT["ALGORITHM"])
            valid_data   = tokenBackend.decode(token, verify = False)
            user_id      = valid_data["user_id"]
        except:
            error_detail = {"detail": "Unauthorized"}
            return Response(error_detail, status = status.HTTP_401_UNAUTHORIZED)

        queryset   = User.objects.get(id = user_id)
        serializer = self.get_serializer(queryset)

        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        tokenData = {
            "email"    : request.data["email"],
            "password" : request.data["password"]
        }

        tokenSerializer = TokenObtainPairSerializer(data = tokenData)
        tokenSerializer.is_valid(raise_exception = True)

        return Response(
            tokenSerializer.validated_data,
            status = status.HTTP_201_CREATED
        )
