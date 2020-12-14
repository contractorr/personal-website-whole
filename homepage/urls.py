"""personal_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""Defines URL patters for our homepage."""
from django.urls import path # We meed the path function to map URLs to views
from . import views # import the views module from this directory


app_name = 'homepage'
# Here urlpatterns represents the pages that can be requested from the learning_logs app
urlpatterns = [
    # The below means that the base URL will trigger the index view function, and this function will be referred to as 'index' in other code sections
    path('', views.index, name='index'),
    path('home', views.index, name='index'),    
    path('project_1.html', views.project_1, name='project_1'),
    path('project_2.html', views.project_2, name='project_2'),
    path('project_3.html', views.project_3, name='project_3'),        
    path('contact', views.send_message, name='send_message'),
]