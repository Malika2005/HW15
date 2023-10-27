from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.filter(status=False).order_by('deadline_date', '-priority')
    completed_tasks = Task.objects.filter(status=True).order_by('-priority')
    context = {'tasks': tasks, 'completed_tasks': completed_tasks}
    return render(request, 'task/task_list.html', context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task/create_task.html', {'form': form})

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/edit_task.html', {'form': form, 'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = True
    task.save()
    return redirect('task_list')
