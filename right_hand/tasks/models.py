from datetime import datetime


from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Sum

from core.models import AbstarctTaskModel
from contacts.models import Contact, Company, Communication

PROJECT_STATUS = [
    ('В работе', 'В работе'),
    ('Завершен', 'Завершен'),
]

INTEREST_STATUS = [
    ('Получена заявка', 'Получена заявка'),
    ('На стороне клиента', 'На стороне клиента'),
    ('На моей стороне', 'На моей стороне'),
    ('Завершен сделкой', 'Завершен сделкой'),
    ('Потерян', 'Потерян'),
]


class BacklogTask(models.Model):
    name = models.CharField(
        "Текст задачи",
        max_length=200,
        help_text="Что нужно сделать?",
    )
    description = models.TextField(
        "Описание задачи",
        help_text="Добавьте описание",
        null=True,
        blank=True,
    )
    plan_pomodoro = models.SmallIntegerField(
        "Временная сложность задачи",
        help_text="Укажите, кол-во 30-минутных отрезков на задачу"
    )
    #  _________________service_________________
    pub_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    last_edit_date = models.DateTimeField(
        'Дата последнего сохранения.',
        auto_now=True,
    )
    priority = models.SmallIntegerField(
        "Приоритет задачи",
    )

    class Meta:
        ordering = ("deadline",)
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Criterion(models.Model):
    """Критерий цели."""
    name = models.CharField(
        "Критерий",
        max_length=200,
        help_text="Уажите критерий.",
    )


class Goal(models.Model):
    """Модель цели"""
    name = models.CharField(
        "Цель",
        max_length=200,
        help_text="Уажите цель.",
    )
    deadline = models.DateTimeField(
        "Дедлайн цели",
        help_text="Дедлайн цели.",
    )
    criterion = models.ManyToManyField(
        Criterion
    )


class Project(AbstarctTaskModel):
    """Модель проекта."""
    revenue = models.IntegerField(
        "Выручка от проекта.",
        help_text="Укажите выручку.",
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
        blank=True,
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


class Interest(models.Model):
    """Модель интереса."""
    revenue = models.IntegerField(
        "Выручка от проекта.",
        help_text="Укажите выручку.",
    )
    partner = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="interests",
        verbose_name="Заказчик",
        help_text="Укажите заказчика.",
    )
    status = models.CharField(
        "Статус интереса",
        choices=INTEREST_STATUS,
        max_length=200,
        help_text="Статус интереса.",
    )
    main_contact = models.ForeignKey(
        Contact,
        on_delete=models.SET_NULL,
        related_name="interests",
        verbose_name="Основной контакт",
        help_text="Укажите контакт который работает в этой компании.",
        null=True,
    )

    def __str__(self):
        return f"Интерес - {self.name}"


class Task(models.Model):
    """Модель задачи."""

    CREATE = 'CR'
    IN_PROGRESS = 'PR'
    DONE = 'DN'
    CANCELED = 'CL'
    TASK_STATUS = [
        (CREATE, 'Cоздана'),
        (IN_PROGRESS, 'В работе'),
        (DONE, 'Выполнена'),
        (CANCELED, 'Отменена'),
    ]

    routine = models.BooleanField(
        verbose_name="Повторяющаяся задача?"
    )
    plan_pomodoro = models.SmallIntegerField(
        "Временная сложность задачи",
        help_text="Укажите, кол-во 30-минутных отрезков на задачу."
    )
    regularity = models.SmallIntegerField(
        "Регулярность",
        default=1,
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Проект",
        help_text="Задача проекта.",
        null=True,
        blank=True,
    )
    interest = models.ForeignKey(
        Interest,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Интерес",
        help_text="Укажите к какому интересу относится задача.",
        null=True,
        blank=True,
    )
    status = models.CharField(
        "Статус задачи",
        choices=TASK_STATUS,
        max_length=40
    )
    top_task = models.ForeignKey(
        'self',
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='down_tasks',
        verbose_name='Родительская задача',
    )

    def clean(self):

        if self.status not in self.TASK_STATUS.values():
            raise ValidationError(
                "Такого статуса нет.")

        if self.top_task and check_deadline_subtask(
            self.top_task.deadline,
            self.deadline
        ):
            raise ValidationError(
                "Дедлайн не может быть позже родительской")

    class Meta:
        ordering = ("deadline",)
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return f"Задача - {self.name} - Дедлайн - {self.deadline}"

    @property
    def time_routine_in_day(self):
        if self.routine:
            return self.plan_pomodoro / self.regularity
        return self.plan_pomodoro

    @property
    def routine_message(self):
        """
        Сообщение о регулярности задачи
        """
        def get_ending(nums):
            num = str(nums).split()[-1]
            if num == '1':
                return 'день'
            if int(num) < 5:
                return 'дня'
            return 'дней'
        if self.routine:
            return (f'Повторяется раз в {self.regularity}'
                    f'{get_ending(self.regularity)}')
        pass

    @property
    def pomodoro_message(self):
        """
        Сообщение о времени выполнения задачи
        """
        real_num_pom = 0
        if self.down_tasks.exists():
            real_num_pom = self.down_tasks.aggregate(
                num_pom=Sum('plan_pomodoro'))["num_pom"]
        num = max([real_num_pom, self.plan_pomodoro])
        if num == 1:
            return '30 минут'
        if num % 2 == 1:
            return f'{num//2} часов 30 минут'
        if num == 2:
            return '1 час'
        return f'{num//2} часов'


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


class CommunicationInterest(models.Model):
    """Модель для связи интереса и контакта."""
    communication = models.ForeignKey(
        Communication,
        on_delete=models.CASCADE,
        related_name="interest",
        verbose_name="Коммуникация.",
        help_text="Укажите коммуникацию."
    )
    interest = models.ForeignKey(
        Interest,
        on_delete=models.CASCADE,
        related_name="communications",
        verbose_name="Интерес.",
        help_text="Укажите интерес."
    )


class CommunicationProject(models.Model):
    """Модель для связи проекта и контакта."""
    communication = models.ForeignKey(
        Communication,
        on_delete=models.CASCADE,
        related_name="project",
        verbose_name="Коммуникация.",
        help_text="Укажите коммуникацию."
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="communications",
        verbose_name="Интерес.",
        help_text="Укажите проект."
    )
