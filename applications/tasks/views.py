""" tasks views module """

# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

# Local
from .models import TasksModel
from .operations import SoapInts

# Create your views here.
def index(request):
    """ index test module """

    if request.method == 'GET':

        context = {
            'tasks': TasksModel.objects.all()
        }

        return render(request, 'index.html', context)
