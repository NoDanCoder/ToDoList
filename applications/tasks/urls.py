""" tasts application urls module """

# Django
from django.urls import path

# Local
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
]
