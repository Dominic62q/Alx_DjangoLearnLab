from bookshelf.models import Book

# Retrieve the book you created earlier
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()
# Expected output: <QuerySet []>  # (empty, meaning the book is deleted)
