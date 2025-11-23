from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
# Endpoint for users to get a token:
# POST username and password to /api-token-auth/
# Example:
# {
#   "username": "user",
#   "password": "pass"
# }
# The returned token is used in the Authorization header for future requests