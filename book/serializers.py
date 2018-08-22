from rest_framework import serializers
from .models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'title',
            'summary',
            'isbn',
            'author',
            'genre',
            'language',
        )