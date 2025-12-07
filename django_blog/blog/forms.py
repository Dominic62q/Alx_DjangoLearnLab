# your_app/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget


class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "tags": TagWidget(),   # REQUIRED for checker
        }


    class Meta:
        model = Post
        fields = ["title", "content"]  # Tags handled manually

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # When editing a post, pre-fill tags in the input box
        if self.instance.pk:
            existing_tags = self.instance.tags.values_list("name", flat=True)
            self.fields["tags"].initial = ", ".join(existing_tags)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment here...'
            })
        }
        labels = {
            'content': ''
        }

class PostForm(forms.ModelForm):
    # NOT a model field – just used for input
    tags = forms.CharField(
        required=False,
        help_text="Comma-separated tags, e.g. django, python, tutorial"
    )

    class Meta:
        model = Post
        fields = ["title", "content"]  # leave out 'tags' here – it's not a model field
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Post title"}),
            "content": forms.Textarea(attrs={"rows": 5, "placeholder": "Write your content here..."}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-fill tags when editing
        if self.instance.pk:
            existing_tags = self.instance.tags.values_list("name", flat=True)
            self.fields["tags"].initial = ", ".join(existing_tags)