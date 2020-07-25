from django.shortcuts import render, get_object_or_404
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

        context = {'task': task}
        return render(request, 'task_view.html', context)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])



