# LibraryProject/bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm, CustomUserForm
from .forms import Example
from .forms import ExampleForm

# ----------------------------
# List all books (requires can_view)
# ----------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# ----------------------------
# Add a new book (requires can_create)
# ----------------------------
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  # Handles uploaded files if any
        if form.is_valid():
            form.save()  # Safe ORM save, prevents SQL injection
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})

# ----------------------------
# Edit an existing book (requires can_edit)
# ----------------------------
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})

# ----------------------------
# Delete a book (requires can_delete)
# ----------------------------
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

# ----------------------------
# Search books safely (requires can_view)
# ----------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)  # ORM prevents SQL injection
    return render(request, 'bookshelf/book_list.html', {'books': books, 'query': query})

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Just a placeholder action to satisfy the assignment
            example_value = form.cleaned_data['example_field']
            print("ExampleForm submitted:", example_value)
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
