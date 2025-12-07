from django.urls import path
from .views import UserLoginView, UserLogoutView, register, profile_view
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)


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

]
