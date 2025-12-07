1. Overview

This authentication system allows users to register, log in, log out, and manage their profile. It uses Django's built-in authentication along with custom registration and profile management features.

2. Components
Component	Location	Purpose
Login View	views.py	Authenticate users
Logout View	views.py	End user session
Registration View	views.py	Create new accounts
Profile View	views.py	View & update account details
Templates	templates/*.html	User interface pages
Forms	forms.py	Input validation
3. URL Paths
Path	Purpose
/auth/login/	Login page
/auth/logout/	Logout
/auth/register/	Create an account
/auth/profile/	View/update account
4. Security Notes

Passwords hashed via Django’s auth system

CSRF protection enabled on all forms

Profile requires authentication

User session secured by Django middleware

5. Testing Instructions

Register a new user

Login with the new account

Logout

Update profile information

Attempt invalid inputs to verify validation

## Blog Post Management (CRUD)

This project implements full CRUD operations for blog posts:

- **ListView** (`PostListView`): `/posts/` – displays all posts.
- **DetailView** (`PostDetailView`): `/posts/<int:pk>/` – shows a single post.
- **CreateView** (`PostCreateView`): `/posts/new/` – authenticated users can create posts.
- **UpdateView** (`PostUpdateView`): `/posts/<int:pk>/edit/` – only the author can edit.
- **DeleteView** (`PostDeleteView`): `/posts/<int:pk>/delete/` – only the author can delete.

Permissions:
- List + detail are public.
- Create requires authentication (`LoginRequiredMixin`).
- Edit/Delete require the user to be the author (`UserPassesTestMixin`).

Posts are linked to the built-in Django `User` model via a ForeignKey (`author`).
