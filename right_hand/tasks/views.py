from django.shortcuts import render

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
