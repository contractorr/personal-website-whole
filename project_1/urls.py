from django.urls import path # We meed the path function to map URLs to views
from . import views # import the views module from this directory

app_name = 'project_1'
# Here urlpatterns represents the pages that can be requested from the learning_logs app
urlpatterns = [
    # The below means that the base URL will trigger the index view function, and this function will be referred to as 'index' in other code sections 
    path('project_1/', views.project_1, name='project_1'), 
    path('plot/', views.plot_graph, name='plot_graph'),
]