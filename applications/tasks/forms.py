""" tasks model > form module """

# Django
from django.forms import ModelForm
from .models import TasksModel

class TasksForm(ModelForm):
    """ class for convert task model to form """

    class Meta:

        model = TasksModel
        fields = ('title', 'description', 'estimated_time', 'worked_time')
