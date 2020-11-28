""" tasks views module """
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """ index test module """
    return render(request, 'index.html')
