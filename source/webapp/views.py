from django.shortcuts import render
from webapp.models import *
from django.http import HttpResponseNotAllowed


def index_view(request):
    data = Task.objects.all()
    return render(request, 'index.html', context={'tasks': data})



