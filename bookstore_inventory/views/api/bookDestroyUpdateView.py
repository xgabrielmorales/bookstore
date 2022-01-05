# Django Rest Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
# Local
from bookstore_inventory.models.book import Book
from bookstore_inventory.serializers import BookSerializer


class BookDestroyUpdateView(GenericAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        instance = Book.objects.get(id=kwargs["pk"])

        serializer = self.get_serializer(instance, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = Book.objects.get(id=kwargs["pk"])
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
