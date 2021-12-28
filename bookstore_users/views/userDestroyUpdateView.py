# Django
from django.conf import settings
# Django REST Framework
from rest_framework.generics    import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response    import Response
from rest_framework             import status
# Django REST Framework Simple JWT
from rest_framework_simplejwt.backends import TokenBackend
# Local
from bookstore_users.models.user import User
from bookstore_users.serializers import UserSerializer

class UserDestroyUpdateView(GenericAPIView):
    serializer_class   = UserSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION").split(" ")[1]
        tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT["ALGORITHM"])
        valid_data = tokenBackend.decode(token, verify = False)
        user_id = valid_data["user_id"]

        if kwargs["pk"] != user_id:
            return Response(status = status.HTTP_401_UNAUTHORIZED)

        instance   = User.objects.get(id = user_id)
        serializer = self.get_serializer(
            instance,
            data = request.data,
        )

        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION").split(" ")[1]
        tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT["ALGORITHM"])
        valid_data = tokenBackend.decode(token, verify = False)
        user_id = valid_data["user_id"]

        if kwargs["pk"] != user_id:
            return Response(status = status.HTTP_401_UNAUTHORIZED)

        instance = User.objects.get(id = user_id)
        instance.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)
