from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def create(request):
    return render(request, 'main/create.html')


