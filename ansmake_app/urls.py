"""
Modules to register the urls with functions
"""
from django.urls import path
from .import views

urlpatterns = [
    path('new', views.createTask, name='create-task'),
    path('all', views.viewTasks, name='view-task'),
]