from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/list.html', context)