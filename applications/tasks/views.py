""" tasks views module """

# Django
from django.shortcuts import render
from django.http import HttpResponse

# Local
from .models import TasksModel
from .forms import TasksForm
from .operations import SoapInts

# Create your views here.
def index(request):
    """ index shows tasks function """

    if request.method == 'GET':

        context = {
            'tasks': TasksModel.objects.all()
        }

        return render(request, 'index.html', context)

def create(request):
    """ create tasks function """

    if request.method == 'GET':

        context = {
            'form': TasksForm()
        }

        return render(request, 'create.html', context)
