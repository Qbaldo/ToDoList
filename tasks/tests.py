from django.test import TestCase
from django.urls import reverse

from .models import Tag, Task


class TaskModelTests(TestCase):

    def test_create_task(self):
        task = Task.objects.create(content="Test task")

        self.assertEqual(task.content, "Test task")
        self.assertFalse(task.is_done)
        self.assertIsNone(task.deadline)

    def test_task_can_have_multiple_tags(self):
        task = Task.objects.create(content="Test task")

        tag1 = Tag.objects.create(name="Python")
        tag2 = Tag.objects.create(name="Django")

        task.tags.add(tag1, tag2)

        self.assertEqual(task.tags.count(), 2)


class TaskViewTests(TestCase):

    def test_task_list(self):
        response = self.client.get(reverse("tasks:task-list"))

        self.assertEqual(response.status_code, 200)

    def test_tag_list(self):
        response = self.client.get(reverse("tasks:tag-list"))

        self.assertEqual(response.status_code, 200)

    def test_task_create(self):
        response = self.client.post(
            reverse("tasks:task-create"),
            {"content": "New task", "deadline": "", "tags": []},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)

    def test_task_toggle(self):
        task = Task.objects.create(content="Test task")

        self.assertFalse(task.is_done)

        response = self.client.get(
            reverse("tasks:task-toggle", args=[task.pk])
        )

        task.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertTrue(task.is_done)
