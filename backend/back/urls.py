from .views import home_view
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view),
    path("faceback/", include("faceback.urls")),
]
