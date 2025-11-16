# LibraryProject/bookshelf/forms.py
from django import forms
from .models import Book, CustomUser

# ----------------------------
# Book Form (secure)
# ----------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author Name'}),
            'publication_year': forms.NumberInput(attrs={'placeholder': 'Year'}),
        }

# ----------------------------
# Custom User Form (optional, for admin/user updates)
# ----------------------------
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth', 'profile_photo']
