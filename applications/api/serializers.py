""" comm JSON <> Dict module """

# Django
from rest_framework import serializers

# Local Utilities
from applications.tasks.models import TasksModel
from applications.tasks.operations import SoapInts

class TaskSerializer(serializers.ModelSerializer):
    """ tasks serializer class """

    class Meta:

        model = TasksModel
        fields = ('title', 'description', 'estimated_time', 'worked_time')

    def create(self, data):
        instance = TasksModel()
        instance.title = data.get('title')
        instance.description = data.get('description')
        instance.estimated_time = data.get('estimated_time')
        instance.worked_time = data.get('worked_time')
        est_time = data.get('estimated_time')
        work_time = data.get('worked_time')
        instance.remaining_time = SoapInts(est_time) - SoapInts(work_time)
        instance.save()
        return instance
