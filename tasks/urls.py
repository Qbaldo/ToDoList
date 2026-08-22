from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("tags/", views.tag_list, name="tag-list"),
    path("tasks/create/", views.task_create, name="task-create"),
    path("tags/create/", views.tag_create, name="tag-create"),
    path("tags/<int:pk>/update/", views.tag_update, name="tag-update"),
    path("tags/<int:pk>/delete/", views.tag_delete, name="tag-delete"),
]
