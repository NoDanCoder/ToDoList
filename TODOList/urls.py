""" TODOList URL Configuration """

# Django
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # Local paths
    path('task/', include('applications.tasks.urls')),
]
