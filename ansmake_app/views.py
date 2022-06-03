"""
Module containing all route functions
"""
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Task
import json


def createTask(request):
    """Function to create a task"""

    #info = {"name": "ope", "email": "ope@gmail.com", "description": "first task"}
    info = request.body
    info = json.loads(info)
    new_task = Task(**info)
    new_task.save()
    return HttpResponse()

def viewTasks(request):
    """Function to view all tasks"""

    task_dict = []
    all_tasks = Task.objects.all()
    for task in all_tasks:
        task_dict.append(task.to_dict())
    
    res = {'data': task_dict}
    res = JsonResponse(res)
    return HttpResponse(res)
