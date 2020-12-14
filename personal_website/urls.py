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
from django.contrib import admin
from django.urls import path, include
# Here we define a urlpatterns variable that represents all sets of all URLS from the apps in the project
urlpatterns = [
    # The below is the URL pattern
    path('admin/', admin.site.urls), # admin.site.urls defines all the URLs that can be requested from the admin site
    path('', include('homepage.urls')) # include the module homepage.urls.
    # This takes 3 arguments .
    ## The first argument is what Django compares to the current request. Django ignores the base url, so '' will match http:/localhost:8000/. Anything else will return an error
    ## The second argument specifies which function to call in views.py when a matching pattern is found.
    ## The thrid argument (not specified above) can be used to provide a name for this URL pattern
]