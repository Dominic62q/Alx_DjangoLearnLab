from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('books/', BookList.as_view(), name='book-List')
]

# Users can obtain a token by POSTing their username and password to /api-token-auth/
# Example POST body:
# {
#   "username": "your_username",
#   "password": "your_password"
# }
# The returned token is used to authenticate future requests.
