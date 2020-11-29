""" tasks views module """

# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models.query_utils import DeferredAttribute

# Views
from django.views.generic import TemplateView

# Local
from .models import TasksModel
from .forms import TasksForm, WorkedTimeForm
from .operations import SoapInts

# Create your views here.

class IndexTasks(TemplateView):
    """ index shows tasks class """

    template_name = 'index.html'
    http_method_names = ('get',)

    def get_context_data(self, **kwargs):
        """ set context data for template """
        
        hidden_columns = ('id', 'estimated_time', 'worked_time')
        return {
            'tasks': TasksModel.objects.all(),
            'tasks_head': (key for key, value in TasksModel.__dict__.items() \
                          if type(value) == DeferredAttribute and key not in hidden_columns)
        }


class CreateTask(TemplateView):
    """ create tasks function """

    template_name = 'create.html'
    http_method_names = ('get', 'post')
    extra_context = {
        'form': TasksForm()
    }

    def post(self, request):

        form = TasksForm(data=request.POST)
       
        if form.is_valid():
            task = form.save(commit=False)
            est_time = task.estimated_time
            work_time = task.worked_time
            task.remaining_time = SoapInts(est_time) - SoapInts(work_time)
            task.save()
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return render(request, 'create.html', self.context)

class EditTask(TemplateView):
    """ edit worked_time property """

    http_method_names = ('post',)

    def post(self, request, id):
    
        form = WorkedTimeForm(request.POST)

        if form.is_valid():
            amount = request.POST['worked_time']
            element = TasksModel.objects.get(id=id)

            work_time = element.worked_time
            element.worked_time = SoapInts(work_time) + SoapInts(amount)

            est_time = element.estimated_time
            work_time = element.worked_time
            element.remaining_time = SoapInts(est_time) - SoapInts(work_time)
            element.save()
            return redirect('index')
        else:
            return HttpResponse(f"invalid {form.errors}")
