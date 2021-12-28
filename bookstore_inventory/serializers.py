from rest_framework import serializers

from .models.book import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Book
        fields = [
            "id",
            "title",
            "author",
            "editorial",
            "gender",
            "num_pages",
            "pub_date",
        ]
