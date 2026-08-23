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

    def test_task_update(self):
        task = Task.objects.create(content="Old content")

        response = self.client.post(
            reverse("tasks:task-update", args=[task.pk]),
            {
                "content": "Updated content",
                "deadline": "",
                "tags": [],
            },
        )

        task.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(task.content, "Updated content")

    def test_task_delete(self):
        task = Task.objects.create(content="Test task")

        response = self.client.post(
            reverse("tasks:task-delete", args=[task.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())

    def test_task_toggle(self):
        task = Task.objects.create(content="Test task")

        self.assertFalse(task.is_done)

        response = self.client.get(
            reverse("tasks:task-toggle", args=[task.pk])
        )

        task.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertTrue(task.is_done)

        self.client.get(
            reverse("tasks:task-toggle", args=[task.pk])
        )

        task.refresh_from_db()

        self.assertFalse(task.is_done)

    def test_tag_create(self):
        response = self.client.post(
            reverse("tasks:tag-create"),
            {"name": "Python"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.first().name, "Python")

    def test_tag_update(self):
        tag = Tag.objects.create(name="Python")

        response = self.client.post(
            reverse("tasks:tag-update", args=[tag.pk]),
            {"name": "Django"},
        )

        tag.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(tag.name, "Django")

    def test_tag_delete(self):
        tag = Tag.objects.create(name="Python")

        response = self.client.post(
            reverse("tasks:tag-delete", args=[tag.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(pk=tag.pk).exists())
