# CRUD Operations for the Book Model

## CREATE
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
<Book: 1984 by George Orwell (1949)>


>>> from bookshelf.models import Book
>>> Book.objects.all()
<QuerySet [<Book: 1984 by George Orwell (1949)>]>
>>> book = Book.objects.get(title="1984")
>>> book.title, book.author, book.publication_year
('1984', 'George Orwell', 1949)
# Retrieved book details successfully


>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book
<Book: Nineteen Eighty-Four by George Orwell (1949)>
# Successfully updated the book title


>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book
<Book: Nineteen Eighty-Four by George Orwell (1949)>
# Successfully updated the book title
