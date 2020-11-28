""" TODOList URL Configuration """

# Django
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


# redefines new default home
def home_url(request):
    """ redicrect home to tasks """
    return redirect('index')


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # Local paths
    path('', home_url),
    path('task/', include('applications.tasks.urls')),
]
