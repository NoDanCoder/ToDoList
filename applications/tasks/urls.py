""" tasts application urls module """

# Django
from django.urls import path

# Local
from .views import IndexTasks, CreateTask, EditTask

urlpatterns = [
    path('', IndexTasks.as_view(), name='index'),
    path('create/', CreateTask.as_view(), name='create'),
    path('edit/<int:id>', EditTask.as_view(), name='edit'),
]
