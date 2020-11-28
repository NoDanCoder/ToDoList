""" tasks app admin module """

# Django
from django.contrib import admin

# Local
from .models import TasksModel

# Register your models here.
@admin.register(TasksModel)
class TasksAdmin(admin.ModelAdmin):
    """ tasks admin class """

    # Table columns
    list_display = ('pk', 'title', 'description', 'estimated_time', 'worked_time')
