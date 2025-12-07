from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog", include("blog.urls")),

    # homepage
    path("", TemplateView.as_view(template_name="blog/dashboard.html"), name="dashboard"),
]
