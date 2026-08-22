from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("tags/", views.tag_list, name="tag-list"),
    path("tasks/create/", views.task_create, name="task-create"),
]
