""" tasks API application urls module """

# Django
from django.urls import path

# Local
from . import api

urlpatterns = [
    path('create/', api.TaskAPI.as_view(), name='api_create'),
]
