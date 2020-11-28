""" tasks views module """

# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

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

    context = {
        'form': TasksForm()
    }

    if request.method == 'GET':
        return render(request, 'create.html', context)

    if request.method == 'POST':

        dictPOST = request.POST.copy()
        est_time = request.POST['estimated_time']
        work_time = request.POST['worked_time']
        dictPOST['remaining_time'] = SoapInts(est_time) - SoapInts(work_time)

        form = TasksForm(dictPOST)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            messages.error(request, 'Some fields are invalid or task title already exist!')
            return render(request, 'create.html', context)
