""" tasks ORM module """

# Django
from django.db import models

# Local Utilities
from .operations import SoapInts

# Create your models here.
class TasksModel(models.Model):
    """ tasks db model """

    title = models.CharField(max_length=32, blank=False, unique=True)
    description = models.TextField(blank=True)
    estimated_time = models.IntegerField(blank=False)
    worked_time = models.FloatField(blank=False)
    remaining_time = models.FloatField(blank=True, null=False, default=0.0)
