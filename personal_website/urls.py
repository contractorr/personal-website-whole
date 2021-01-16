from django.contrib import admin
from django.urls import path, include
from homepage import views
from portfolio import views

urlpatterns = [
    path('', include('homepage.urls')),
    path('', include('portfolio.urls')),
    path('admin/', admin.site.urls),
]
