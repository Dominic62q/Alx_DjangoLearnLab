from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListViewSet

router = DefaultRouter()
router.register(r'books_all', BookListViewSet, basename='book_all')


urlpatterns = [
    path('', include(router.urls)),    # Maps to the BookList view
]