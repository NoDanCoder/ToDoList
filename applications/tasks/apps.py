""" app entry point module """

# Django
from django.apps import AppConfig


class TasksConfig(AppConfig):
    """ class label app """
    name = 'tasks'
    verbose_name = 'Tasks'
