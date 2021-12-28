# Django Rest Framework
from rest_framework             import status
from rest_framework.response    import Response
from rest_framework.generics    import GenericAPIView
from rest_framework.permissions import IsAuthenticated
# Local
from bookstore_inventory.models.book import Book
from bookstore_inventory.serializers import BookSerializer

class BookListCreateView(GenericAPIView):
    queryset           = Book.objects.all()
    serializer_class   = BookSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset   = self.get_queryset()
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
