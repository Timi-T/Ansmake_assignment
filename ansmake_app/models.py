"""
Module to define data models
"""
from django.db import models
from uuid import uuid4
from django.utils import timezone


class Task(models.Model):
    """
    Class that defines a task
    Class attributes include;
        - Task name
        - Task description
        - Email address
        - Task ID
        - createdAt
    """

    id = models.TextField(default=str(uuid4()), primary_key=True)
    name = models.TextField()
    email = models.EmailField()
    description = models.TextField()
    createdAt = models.DateTimeField(default=timezone.now)

    def to_dict(self):
        """
        Method to get the dictionary representation of a task
        """

        self_dict = {}
        self_dict['id'] = self.id
        self_dict['name'] = self.name
        self_dict['description'] = self.description
        self_dict['email'] = self.email
        self_dict['createdAt'] = self.createdAt

        return self_dict