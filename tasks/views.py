from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm


def index(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    tasks = Task.objects.all()
    context = {"tasks": tasks, "task_form": form}
    return render(request, "tasks/tasks.html", context=context)


def update_task(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return redirect("/")

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TaskForm(instance=task)

    context = {"task": task, "task_form": form}
    return render(request, "update_task/update_task.html", context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("/")

    context = {"task": task}
    return render(request, "update_task/delete_task.html", context=context)
