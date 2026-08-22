from django.shortcuts import get_object_or_404, redirect, render

from .models import Tag, Task
from .forms import TaskForm, TagForm


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
    tags = Tag.objects.all()

    return render(request, "tasks/tag_list.html", {"tags": tags})

def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("tasks:tag-list")
    else:
        form = TagForm()

    return render(request, "tasks/tag_form.html", {"form": form})

def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)

    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)

        if form.is_valid():
            form.save()
            return redirect("tasks:tag-list")
    else:
        form = TagForm(instance=tag)

    return render(request, "tasks/tag_form.html", {"form": form})

def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)

    if request.method == "POST":
        tag.delete()
        return redirect("tasks:tag-list")

    return render(request, "tasks/tag_confirm_delete.html", {"tag": tag})
