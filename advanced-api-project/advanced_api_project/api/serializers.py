from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# BookSerializer:
# Serializes all fields in the Book model.
# Includes validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

    # Custom validation: year must NOT be in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer:
# Serializes an Author AND their related Books.
# Uses nested serialization:
# - Each Author will include a list of BookSerializer items
# - Uses related_name='books' from the Book model.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  
    # "books" is the reverse relation: author.book_set.all()

    class Meta:
        model = Author
        fields = ["name", "books"]
