from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import *
from django.http import HttpResponseNotAllowed
from .forms import TaskForm


def index_view(request):
    data = Task.objects.all()
    return render(request, 'index.html', context={'tasks': data})


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)


def task_create_view(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'task_create.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                date=form.cleaned_data['date'])
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_create.html', context={'form': form})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'date': task.date
        })
        return render(request, 'update.html', context={'task': task, 'form': form})

    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title'],
            task.description = form.cleaned_data['description'],
            task.status = form.cleaned_data['status'],
            task.date = form.cleaned_data['date']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update.html', context={'task': task, 'form': form})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


