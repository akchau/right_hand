from datetime import datetime

from django.db import models

from contacts.models import Company, Contact

PROJECT_STATUS = [
    ('В работе', 'В работе'),
    ('Завершен', 'Завершен'),
]


class Project(models.Model):
    """Модель проекта."""
    name = models.CharField(
        "Название проекта.",
        max_length=200,
        help_text="Название проекта.",
    )
    revenue = models.IntegerField(
        "Выручка от проекта.",
        help_text="Укажите выручку.",
    )
    deadline = models.DateField(
        "Дедлайн.",
        help_text="Дедлайн.",
    )
    my_role = models.CharField(
        "Роль в проекте.",
        max_length=200,
        help_text="Роль в проекте.",
    )
    customer = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        related_name="projects",
        verbose_name="Заказчик",
        help_text="Укажите заказчика.",
        null=True,
    )
    status = models.CharField(
        "Статус проекта",
        choices=PROJECT_STATUS,
        max_length=200,
        help_text="Статус проекта.",
    )

    class Meta:
        ordering = ("deadline",)
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    @property
    def is_expired(self):
        if datetime.today().timestamp() > self.deadline.timestamp():
            return True
        return False

    def __str__(self):
        return self.name


class Task(models.Model):
    """Модель задачи."""
    name = models.CharField(
        "Тескт задачи",
        max_length=200,
        help_text="Что нужно сделать.",
    )
    deadline = models.DateTimeField(
        "Дедлайн задачи.",
        help_text="Дедлайн задачи.",
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Проект",
        help_text="Укажите к какому проекту относится задача.",
        null=True,
    )

    class Meta:
        ordering = ("deadline",)
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    @property
    def is_expired(self):
        if datetime.today().timestamp() > self.deadline.timestamp():
            return True
        return False

    def __str__(self):
        return f"Задача - {self.name} - Дедлайн - {self.deadline}"


class ProjectContact(models.Model):
    """Класс устанавливающий связь проекта с контактами."""
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="contact_project",
        verbose_name="Проект",
        help_text="Укажите проект контакта."
    )
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name="contact_project",
        verbose_name="Контакт",
        help_text="Укажите контакт проекта."
    )
    role = models.CharField(
        "Роль в проекте.",
        max_length=200,
        help_text="Роль в проекте.",
    )

    def __str__(self):
        return f"{self.project} - {self.contact}"
