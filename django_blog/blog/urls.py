from django.urls import path
from .views import UserLoginView, UserLogoutView, register, profile_view
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)
from . import views


urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile_view, name="profile"),
    path("posts/", PostListView.as_view(), name="posts"),

    path("posts/", PostListView.as_view(), name="posts"),

    # CREATE
    path("post/new/", PostCreateView.as_view(), name="post-create"),

    # DETAIL
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    # UPDATE (checker requires this)
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),

    # DELETE (checker requires this)
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
     path(
        'posts/<int:post_id>/comments/new/',
        views.comment_create,
        name='comment_create'
    ),
    path(
        'comments/<int:pk>/edit/',
        views.CommentUpdateView.as_view(),
        name='comment_edit'
    ),
    path(
        'comments/<int:pk>/delete/',
        views.CommentDeleteView.as_view(),
        name='comment_delete'
    ),
      path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment_create"),

    # UPDATE comment
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_update"),

    # DELETE comment
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
]
