from django.contrib import admin
from django.urls import path, include  # ✅ include must be imported
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
]
