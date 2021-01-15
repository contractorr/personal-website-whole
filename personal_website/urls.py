from django.contrib import admin
from django.urls import path, include
from homepage import views
from project_1 import views

urlpatterns = [
    path('', include('homepage.urls')),
    path('', include('project_1.urls')),
    path('admin/', admin.site.urls),
]
