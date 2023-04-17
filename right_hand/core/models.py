from django.db import models

from core.timer.timer import (get_is_expired,
                               get_time_created_message,
                               get_time_left_message,
                               get_time_updtaed_message)


class AbstarctTaskModel(models.Model):
    """Абстрактная модель. Добавляет """
    name = models.CharField(
        "Тескт задачи",
        max_length=200,
        help_text="Что нужно сделать?",
    )
    description = models.TextField(
        "Описание задачи",
        help_text="Добавьте описание",
        null=True,
        blank=True,
    )
    deadline = models.DateTimeField(
        "Дедлайн задачи",
        help_text="Когда дедлайн?",
    )
    pub_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    last_edit_date = models.DateTimeField(
        'Дата последнего сохранения.',
        auto_now=True,
    )
    done_date = models.DateTimeField(
        "Дата выполнения",
        null=True,
        blank=True
    ),

    class Meta:
        abstract = True

    @property
    def created_time_message(self):
        """
        Сообщение об прошедшем с даты создания
        Возвращает str
        """
        return get_time_created_message(self.deadline)

    @property
    def updated_time_message(self):
        """
        Сообщение об прошедшем с даты создания
        Возвращает str
        """
        return get_time_updtaed_message(self.deadline)

    @property
    def is_expired(self):
        """
        Сообщение об оставшемся или просроченом
        времени относительно текущего времени
        Возвращает bool
        """
        return get_is_expired(self.deadline)

    @property
    def time_left_message(self):
        """
        Сообщение об оставшемся или просроченом
        времени относительно текущего времени
        Возвращает str
        """
        return get_time_left_message(self.deadline)
