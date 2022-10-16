from django.shortcuts import render, get_object_or_404, redirect

from contacts.models import Company
from .forms import TaskForm, ProjectForm, InterestForm, InterestFormWithPartner
from .models import Task, Project, Interest


def tasks(request):
    """Все задачи."""
    template = "tasks/tasks.html"
    title = 'Мои задачи.'
    header = title
    tasks = Task.objects.all().order_by(
        "deadline")
    context = {
        'title': title,
        'header': header,
        'tasks': tasks,
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


def task_new(request):
    """Добавление нового контакта."""
    form = TaskForm(
        request.POST or None,
    )
    if form.is_valid():
        form.save()
        return redirect("tasks:tasks")
    template = "tasks/task_new.html"
    title = "Новая задача."
    action = "Добавьте новую задачу."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
    }
    return render(request, template, context)


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(
        request.POST or None,
        files=request.FILES or None,
        instance=task,
    )
    if form.is_valid():
        form.save()
        return redirect("tasks:task_profile", pk=pk)
    title = "Редактирование задачи."
    header = title
    action = "Редактируйте задачу"
    template = "tasks/task_new.html"
    context = {
        "title": title,
        "header": header,
        "action": action,
        "form": form,
        "is_edit": True,
        "pk": pk,
    }
    return render(request, template, context)


def task_delete(request, pk):
    Task.objects.get(pk=pk).delete()
    return redirect("tasks:tasks")


def projects(request):
    """Все проекты."""
    template = "tasks/projects.html"
    title = 'Мои проекты.'
    header = title
    projects = Project.objects.all().order_by(
        "deadline")
    context = {
        'title': title,
        'header': header,
        'projects': projects,
    }
    return render(request, template, context)


def project_profile(request, pk):
    """Страничка проекта."""
    template = "tasks/project_profile.html"
    project = get_object_or_404(Project, pk=pk)
    title = f'Проект - {project.name}'
    header = title
    context = {
        'title': title,
        'header': header,
        'project': project,
    }
    return render(request, template, context)


def project_new(request):
    """Добавление нового проекта."""
    form = ProjectForm(
        request.POST or None,
    )
    if form.is_valid():
        new_project = form.save(commit=False)
        new_project.status = "В работе"
        form.save()
        return redirect("tasks:projects")
    template = "tasks/project_new.html"
    title = "Новый проект."
    action = "Добавьте новый проект."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
    }
    return render(request, template, context)


def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(
        request.POST or None,
        files=request.FILES or None,
        instance=project,
    )
    if form.is_valid():
        form.save()
        return redirect("tasks:project_profile", pk=pk)
    title = "Редактирование проекта."
    header = title
    action = "Редактируйте информацию по проекту."
    template = "tasks/project_new.html"
    context = {
        "title": title,
        "header": header,
        "action": action,
        "form": form,
        "is_edit": True,
        "pk": pk,
    }
    return render(request, template, context)


def project_delete(request, pk):
    Project.objects.get(pk=pk).delete()
    return redirect("tasks:projects")


def interests(request):
    """Все интересы."""
    template = "tasks/interests.html"
    title = 'Мои интересы.'
    header = title
    interests = Interest.objects.all().order_by(
        "revenue")
    context = {
        'title': title,
        'header': header,
        'interests': interests,
    }
    return render(request, template, context)


def interest_profile(request, pk):
    """Страничка интереса."""
    template = "tasks/interest_profile.html"
    interest = get_object_or_404(Interest, pk=pk)
    title = f'Интерес - {interest.name}'
    header = title
    context = {
        'title': title,
        'header': header,
        'interest': interest,
    }
    return render(request, template, context)


def interest_new(request):
    """Добавление нового интреса."""
    form = InterestForm(
        request.POST or None,
    )
    if form.is_valid():
        new_interest = form.save(commit=False)
        new_interest.status = 'Получена заявка'
        new_interest = form.save()
        return redirect("tasks:interest_profile", pk=new_interest.pk)
    template = "tasks/interest_new.html"
    title = "Новый интерес c компанией."
    action = "Добавьте новый интерес."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
    }
    return render(request, template, context)


def interest_new_with_partner(request, pk):
    """Добавление нового интреса c партнером."""
    partner = get_object_or_404(Company, pk=pk)
    form = InterestFormWithPartner(
        request.POST or None,
    )
    if form.is_valid():
        new_interest = form.save(commit=False)
        new_interest.status = 'Получена заявка'
        new_interest.partner = partner
        new_interest = form.save()
        return redirect("tasks:interest_profile", pk=new_interest.pk)
    template = "tasks/interest_new.html"
    title = "Новый интерес."
    action = "Добавьте новый интерес."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
        "with_partner": True,
        "pk": pk
    }
    return render(request, template, context)


def interest_edit(request, pk):
    interest = get_object_or_404(Interest, pk=pk)
    form = InterestForm(
        request.POST or None,
        files=request.FILES or None,
        instance=interest,
    )
    if form.is_valid():
        form.save()
        return redirect("tasks:interest_profile", pk=pk)
    title = "Редактирование интереса."
    header = title
    action = "Редактируйте информацию интереса."
    template = "tasks/interest_new.html"
    context = {
        "title": title,
        "header": header,
        "action": action,
        "form": form,
        "is_edit": True,
        "pk": pk,
    }
    return render(request, template, context)


def interest_delete(request, pk):
    Interest.objects.get(pk=pk).delete()
    return redirect("tasks:interests")
