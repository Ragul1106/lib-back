from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    book_age = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_year', 'book_age']


    def get_book_age(self, obj):
        return date.today().year - obj.published_year

    def validate_published_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Published year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']