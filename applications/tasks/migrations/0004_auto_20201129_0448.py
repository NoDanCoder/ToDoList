# Generated by Django 3.1.3 on 2020-11-29 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_tasksmodel_remaining_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksmodel',
            name='remaining_time',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
