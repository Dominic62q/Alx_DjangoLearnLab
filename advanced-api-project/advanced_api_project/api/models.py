from django.db import models

# Author model:
# This model represents a book author.
# One Author can have MANY books (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

# Book model:
# This model stores information for each book.
# Each Book is linked to ONE Author using a ForeignKey.
# The Author → Book relationship:
# - One Author can write multiple Books
# - Each Book belongs to only one Author
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
