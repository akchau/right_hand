from datetime import datetime, timedelta
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect

from contacts.models import Communication, Company
from contacts.forms import CommunicationForm
from contacts.views import plan_communication
from .forms import (TaskForm,
                    ProjectForm,
                    InterestForm,
                    InterestFormWithPartner,
                    TaskFormWithProject,
                    CategoryTaskForm)
from .models import (CommunicationProject,
                     Task, Project,
                     Interest,
                     CommunicationInterest,
                     CategoryTask)


def categories_of_tasks(request):
    """Все категории задач."""
    template = "tasks/categories.html"
    title = 'Категории задач.'
    header = title
    categories = CategoryTask.objects.all().order_by("name")
    context = {
        'title': title,
        'header': header,
        'categories': categories
    }
    return render(request, template, context)


def category_of_task_profile(request, pk):
    """Карточка категории задач."""
    template = "tasks/category_profile.html"
    category = get_object_or_404(CategoryTask, pk=pk)
    tasks = Task.objects.filter(category=category).order_by('-deadline')
    title = f'Категория {category.name}'
    header = title
    context = {
        'title': title,
        'header': header,
        'category': category,
        'tasks': tasks
    }
    return render(request, template, context)


def category_of_task_edit(request, pk):
    category = get_object_or_404(CategoryTask, pk=pk)
    form = CategoryTaskForm(
        request.POST or None,
        files=request.FILES or None,
        instance=category,
    )
    if form.is_valid():
        form.save()
        return redirect("tasks:category_of_task_profile", pk=pk)
    title = "Редактирование категории."
    header = title
    action = "Редактируйте категорию"
    template = "tasks/category_new.html"
    context = {
        "title": title,
        "header": header,
        "action": action,
        "form": form,
        "is_edit": True,
        "pk": pk,
    }
    return render(request, template, context)


def category_of_task_new(request):
    """Добавление нового контакта."""
    form = CategoryTaskForm(
        request.POST or None,
    )
    if form.is_valid():
        form.save()
        return redirect("tasks:categories_of_tasks")
    template = "tasks/category_new.html"
    title = "Новая категория."
    action = "Добавьте новую категорию."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
    }
    return render(request, template, context)


def category_of_task_delete(request, pk):
    CategoryTask.objects.get(pk=pk).delete()
    return redirect("tasks:categories_of_tasks")


def tasks(request):
    """Все задачи."""
    template = "tasks/tasks.html"
    title = 'Мои задачи.'
    header = title
    categories = CategoryTask.objects.all().order_by(
        "name")
    tasks = Task.objects.filter(done=False).order_by(
        "deadline")
    tasks_done = Task.objects.filter(done=True).order_by(
        "-deadline")
    tasks_routine = Task.objects.filter(routine=True, done=False)
    if tasks:
        numbers_pomodoro = tasks.aggregate(
            sum_pomodoro=Sum('plan_pomodoro')
        )
        pomodoro = int(numbers_pomodoro['sum_pomodoro'])
    else:
        pomodoro = 0
    if tasks_routine:
        numbers_pomodoro_routine = tasks_routine.aggregate(
            sum_pomodoro=Sum('plan_pomodoro')
        )
        pomodoro_routine = int(numbers_pomodoro_routine['sum_pomodoro'])
        numbers_pomodoro_routine_day = sum([item.time_routine_in_day for item in tasks_routine])
    else:
        pomodoro_routine = 0
        numbers_pomodoro_routine_day = 0
    context = {
        'title': title,
        'header': header,
        'tasks': tasks,
        'tasks_done': tasks_done,
        'categories': categories,
        'numbers_pomodoro_hours': pomodoro//2,
        'numbers_pomodoro_minutes': (pomodoro % 2) * 30,
        'numbers_pomodoro_routine_hours': pomodoro_routine//2,
        'numbers_pomodoro_routine_minutes': (pomodoro_routine % 2) * 30,
        'numbers_pomodoro_routine_day_hours': numbers_pomodoro_routine_day//2,
        'numbers_pomodoro_routine_day_minutes': (numbers_pomodoro_routine_day % 2) * 30
    }
    return render(request, template, context)


def task_profile(request, pk):
    """Страничка задачи."""
    template = "tasks/task_profile.html"
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    title = task.name
    header = title
    context = {
        'title': title,
        'header': header,
        'task': task,
        'project': project,
    }
    return render(request, template, context)


def task_new(request):
    """Добавление нового контакта."""
    form = TaskForm(
        request.POST or None,
    )
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.done = False
        form.save(commit=True)
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


def task_new_with_project(request, pk):
    """Добавление новой задачи в проекте."""
    project = get_object_or_404(Project, pk=pk)
    form = TaskFormWithProject(
        request.POST or None,
    )
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.project = project
        new_task.done = False
        form.save(commit=True)
        return redirect("tasks:project_profile", pk=pk)
    template = "tasks/task_new.html"
    title = "Новая задача проекта."
    action = f"Добавьте новую задачу для проекта {project.name}."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
        "pk": pk,
        "with_project": True,
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


def task_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.done:
        task.done = False
        if task.routine:
            if Task.objects.filter(name=task.name,
                                   description=task.description,
                                   done=False).exists():
                Task.objects.filter(name=task.name,
                                    description=task.description,
                                    done=False).delete()
        task.save()
        return redirect('tasks:tasks')
    task.done = True
    if task.routine:
        new_task = Task(
            name=task.name,
            description=task.description,
            deadline=datetime.today() + timedelta(
                days=task.regularity
            ),
            project=task.project,
            routine=True,
            regularity=task.regularity,
            done=False
        )
        new_task.save()
    task.save()
    return redirect('tasks:tasks')


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
    communications_id = project.communications.values_list(
        "communication",
        flat=True
    )
    communications = Communication.objects.filter(pk__in=communications_id)
    tasks = Task.objects.filter(project=project)
    title = f'Проект - {project.name}'
    header = title
    context = {
        'title': title,
        'header': header,
        'project': project,
        'tasks': tasks,
        'communications': communications
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
    communications_id = interest.communications.values_list(
        "communication",
        flat=True
    )
    communications = Communication.objects.filter(pk__in=communications_id)
    title = f'Интерес - {interest.name} для {interest.partner}'
    header = title
    context = {
        'title': title,
        'header': header,
        'interest': interest,
        'communications': communications,
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


def new_communicaitions_of_interest(request, pk):
    """Добавление новой коммуникаци в интерес."""
    interest = Interest.objects.get(pk=pk)
    form = CommunicationForm(
        request.POST or None,
    )
    if form.is_valid():
        new_communication = form.save(commit=False)
        new_communication.status = "Выполнено"
        form.save(commit=True)
        interest_communication = CommunicationInterest(
            interest=interest,
            communication=new_communication
        )
        interest_communication.save()
        plan_communication(new_communication.contact)
        return redirect("tasks:interest_profile", pk=pk)
    template = "contacts/communication_new.html"
    title = f"Новая коммуникация интереса - {interest.name}."
    action = "Добавьте новую коммуникацию."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
        "with_interest": True,
        "pk": pk
    }
    return render(request, template, context)


def new_communicaitions_of_project(request, pk):
    """Добавление новой коммуникаци в проект."""
    project = Project.objects.get(pk=pk)
    form = CommunicationForm(
        request.POST or None,
    )
    if form.is_valid():
        new_communication = form.save(commit=False)
        new_communication.status = "Выполнено"
        form.save(commit=True)
        project_communication = CommunicationProject(
            project=project,
            communication=new_communication
        )
        project_communication.save()
        plan_communication(new_communication.contact)
        return redirect("tasks:project_profile", pk=pk)
    template = "contacts/communication_new.html"
    title = f"Новая коммуникация для проекта - {project.name}."
    action = "Добавьте новую коммуникацию."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
        "with_project": True,
        "pk": pk
    }
    return render(request, template, context)
