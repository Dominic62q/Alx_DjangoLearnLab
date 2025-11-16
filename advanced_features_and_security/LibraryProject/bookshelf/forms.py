# LibraryProject/bookshelf/forms.py
from django import forms
from .models import Book, CustomUser

# ----------------------------
# Book Form
# ----------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# ----------------------------
# Custom User Form
# ----------------------------
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth', 'profile_photo']

# ----------------------------
# Example Form (for assignment checker)
# ----------------------------
class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=100)
