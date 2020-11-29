""" tasks views module """

# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models.query_utils import DeferredAttribute

# Local
from .models import TasksModel
from .forms import TasksForm, WorkedTimeForm
from .operations import SoapInts

# Create your views here.
def index(request):
    """ index shows tasks function """

    if request.method == 'GET':

        hidden_columns = ('id', 'estimated_time', 'worked_time')

        context = {
            'tasks': TasksModel.objects.all(),
            'tasks_head': (key for key, value in TasksModel.__dict__.items() \
                          if type(value) == DeferredAttribute and key not in hidden_columns)
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

        form = TasksForm(request.POST)
        
        import pdb; pdb.set_trace()
        if form.is_valid():
            
            dictPOST = request.POST.copy()
            est_time = request.POST['estimated_time']
            work_time = request.POST['worked_time']
            dictPOST['remaining_time'] = SoapInts(est_time) - SoapInts(work_time)

            form = TasksForm(dictPOST)
            form.save()
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return render(request, 'create.html', context)

def edit(request, id):
    """ edit worked_time property """

    form = WorkedTimeForm(request.POST)

    if form.is_valid():
        amount = request.POST['worked_time']
        element = TasksModel.objects.get(id=id)

        work_time = str(element.worked_time)

        element.worked_time = SoapInts(work_time) + SoapInts(amount)

        est_time = str(element.estimated_time)
        work_time = str(element.worked_time)

        element.remaining_time = SoapInts(est_time) - SoapInts(work_time)
        element.save()
        return redirect('index')
    else:
        return HttpResponse('fail')



