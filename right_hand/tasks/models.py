from datetime import datetime

from django.db import models


class Task(models.Model):
    name = models.CharField(
        "Тескт задачи",
        max_length=200,
        help_text="Что нужно сделать.",
    )
    deadline = models.DateTimeField(
        "Планируемая дата коммуникации.",
        help_text="Планируемая дата коммуникации.",
    )

    @property
    def is_expired(self):
        if datetime.today().timestamp() > self.deadline.timestamp():
            return True
        return False

    def __str__(self):
        return f"Задача - {self.name} - Дедлайн - {self.deadline}"
