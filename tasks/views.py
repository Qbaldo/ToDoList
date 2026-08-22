from django.shortcuts import redirect, render

from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.order_by("is_done", "-datetime")

    return render(request, "tasks/task_list.html", {"tasks": tasks})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("tasks:task-list")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form})


def tag_list(request):
    return render(request, "tasks/tag_list.html")