from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # No need for regex here
    path('', include('homepage.urls')),  # No need for regex here
]
