""" tasks ORM module """

# Django
from django.db import models

# Create your models here.
class TasksModel(models.Model):
    """ tasks db model """

    title = models.CharField(max_length=32, blank=False, unique=True)
    description = models.TextField(blank=True)
    estimated_time = models.IntegerField(blank=False)
    worked_time = models.FloatField(blank=False)
    remaining_time = models.FloatField(default=0.0)
