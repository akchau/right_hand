from datetime import datetime, timedelta

from django.db import models

from contacts.models import Contact, Company, Communication


PROJECT_STATUS = [
    ('В работе', 'В работе'),
    ('Завершен', 'Завершен'),
]

TASK_STATUS = [
    ('Создан', 'Создан'),
    ('Требуется разбить на подзадачи', 'Требуется разбить на подзадачи'),
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
    name = models.CharField(
        "Название проекта.",
        max_length=200,
        help_text="Название проекта.",
    )
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
    pub_date = models.DateTimeField(
        "Дата создания.",
        help_text="Дедлайн задачи.",
        auto_now_add=True
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
    name = models.CharField(
        "Тескт задачи",
        max_length=200,
        help_text="Что нужно сделать?",
    )
    deadline = models.DateTimeField(
        "Дедлайн задачи",
        help_text="Когда дедлайн?",
    )
    description = models.TextField(
        "Описание задачи",
        help_text="Добавьте описание",
        null=True,
        blank=True,
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
    routine = models.BooleanField(
        verbose_name="Повторяющаяся задача?"
    )
    regularity = models.SmallIntegerField(
        "Регулярность",
        default=1,
    )
    done = models.BooleanField(
        verbose_name="Выполнена?",
    )
    pub_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    last_edit_date = models.DateTimeField(
        'Дата последнего сохранения.',
        auto_now=True,
    )
    plan_pomodoro = models.SmallIntegerField(
        "Временная сложность задачи",
        help_text="Укажите, кол-во 30-минутных отрезков на задачу."
    )
    priority = models.PositiveSmallIntegerField(
        "Приоритет задачи",
        null=True,
        blank=True,
    )
    done_date = models.DateTimeField(
        "Дата выполнения",
        null=True,
        blank=True
    ),
    status = models.CharField(
        "Статус задачи",
        choices=TASK_STATUS,
        max_length=40
    )
    new = models.BooleanField(
        verbose_name="Новые"
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

    @property
    def time_routine_in_day(self):
        if self.routine:
            return self.plan_pomodoro / self.regularity
        return self.plan_pomodoro

    @property
    def routine_message(self):
        def get_ending(nums):
            num = str(nums).split()[-1]
            if num == '1':
                return 'день'
            if int(num) < 5:
                return 'дня'
            return 'дней'
        if self.routine:
            return (f'Рутина. Раз в {self.regularity}'
                    f'{get_ending(self.regularity)}')
        pass

    @property
    def pomodoro_message(self):
        num = self.plan_pomodoro
        if num == 1:
            return '30 минут'
        if num % 2 == 1:
            return f'{num//2} часов 30 минут'
        if num == 2:
            return '1 час'
        return f'{num//2} часов'

    @property
    def time_left(self):
        now = datetime.now()
        deadline = datetime(
            self.deadline.year,
            self.deadline.month,
            self.deadline.day,
            self.deadline.hour,
            self.deadline.minute,
            self.deadline.second,
        )

        print(now)
        deadline = datetime(
            self.deadline.year,
            self.deadline.month,
            self.deadline.day,
            self.deadline.hour,
            self.deadline.minute,
            self.deadline.second,
        )
        left_time = deadline - now
        left_time = left_time
        # 
        # months = left_time.month
        # days = left_time.day
        # if left_time.day:
            # years = left_time.year
            # if years < 2:
                # mess = f'{years} год'
            # elif years < 5:
                # mess = f'{years} года'
            # else:
                # mess = f'{years} лет'
            # message_params.append(mess)
        # if months > 0:
            # mess = f'{months} мес.'
            # message_params.append(mess)
        # if days > 0:
            # mess = f'{days} д.'
            # message_params.append(mess)
        message = 'Осталось '
        message = f'{message} {left_time} нед.'
        return message

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
