# LibraryProject/bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django import forms

# ----------------------------
# Example: Secure Book Form
# ----------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# ----------------------------
# Add Book View (secure)
# ----------------------------
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)  # Use Django form to validate input
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})

# ----------------------------
# Search Books View (prevent SQL injection)
# ----------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)  # ORM prevents SQL injection
    return render(request, 'bookshelf/book_list.html', {'books': books})
