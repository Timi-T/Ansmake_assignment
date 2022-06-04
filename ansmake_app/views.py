"""
Module containing all route functions
"""
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json


@csrf_exempt
def createTask(request):
    """Function to create a task"""

    data = request.body
    data = json.loads(data)
    info = {}
    name = info['name'] = data.get('name')
    email = info['email'] = data.get('email')
    description = info['description'] = data.get('description')
    if not description:
        info['description'] = ''
    if name and email:
        new_task = Task(**info)
        new_task.save()
    return HttpResponse(new_task.name)

def viewTasks(request):
    """Function to view all tasks"""

    task_list = []
    all_tasks = Task.objects.all()
    for task in all_tasks:
        """Converting all the objects in the list to dictionaries"""
        task_list.append(task.to_dict())
        """
        to_dict is a method created to convert a 'Task' object to a dictionary
        """
    
    res = {'data': task_list}
    res = JsonResponse(res)
    return HttpResponse(res)
