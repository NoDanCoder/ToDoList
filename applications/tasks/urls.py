""" tasts application urls module """

# Django
from django.urls import path

# Local
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
