from django.shortcuts import render, get_object_or_404

from .models import Task


def tasks(request):
    """Все задачи."""
    template = "tasks/tasks.html"
    title = 'Мои задачи.'
    header = title
    contacts = Task.objects.all().order_by(
        "deadline")
    context = {
        'title': title,
        'header': header,
        'contacts': contacts,
    }
    return render(request, template, context)


def task_profile(request, pk):
    """Страничка задачи."""
    template = "tasks/task_profile.html"
    task = get_object_or_404(Task, pk=pk)
    title = f'{task.name} - {task.deadline}'
    header = title
    context = {
        'title': title,
        'header': header,
        'task': task,
    }
    return render(request, template, context)
