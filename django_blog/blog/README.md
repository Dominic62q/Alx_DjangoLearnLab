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

Comment System Overview

Each Post can have many Comment objects (one-to-many).

Each Comment belongs to:

a Post (ForeignKey)

a User as author (ForeignKey)

The system tracks created_at and updated_at for auditing.

How to Add a Comment

Go to a post detail page: /posts/<post_id>/.

If logged in, a comment form appears at the bottom of the page.

Type your message and submit.

You are redirected back to the post with your new comment visible.

How to Edit a Comment

Only the author of a comment can edit it.

On the post detail page, if you are the author, you see an “Edit” link.

Clicking it opens /comments/<comment_id>/edit/.

After saving, you are sent back to the post detail page.

How to Delete a Comment

Only the author of a comment can delete it.

On the post detail page, if you are the author, you see a “Delete” link.

This opens a confirmation page at /comments/<comment_id>/delete/.

Confirming deletion removes the comment and redirects you back to the post.

Permissions & Visibility

All users (including anonymous visitors) can view comments under a post.

Only authenticated users can create comments.

Only the comment’s author can edit or delete that comment.

Permissions are enforced both:

in the template (show/hide buttons)

in the views (using @login_required and UserPassesTestMixin).