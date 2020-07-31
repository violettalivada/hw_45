from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import *
from django.http import HttpResponseNotAllowed


def index_view(request):
    data = Task.objects.all()
    return render(request, 'index.html', context={'tasks': data})


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)


def task_create_view(request):
    if request.method == "GET":
        return render(request, 'task_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        date = request.POST.get('date')
        if date == '':
            date = None
        task = Task.objects.create(title=title, description=description,
                                   status=status, date=date)

        return redirect('task_view', pk=task.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', context={'task': task})

    elif request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('task_view', pk=task.pk)
