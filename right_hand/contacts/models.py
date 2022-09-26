from django.db import models

TYPE_OF_COMMUNICATIONS = [
    ('Phone', 'Phone'),
    ('Meeting', 'Meeting'),
    ('Chat', 'Chat'),
    ('Video', 'Video'),
]


class Contact(models.Model):
    """Модель контакта."""

    name = models.CharField(
        "Имя контакта.",
        max_length=200,
        help_text="Укажите название группы.",
    )
    is_family = models.BooleanField(
        "Член семьи.",
        help_text="Член семьи.",
    )
    email = models.EmailField(default="email@email.ru")
    frequency_of_communications_days = models.IntegerField(blank=True)
    date_of_birthday = models.DateTimeField(
        "Дата рождения.",
        blank=True,
        default="2011-09-29"
    )


class Communication(models.Model):
    """Модель коммуникации."""

    type = models.CharField(
        max_length=10,
        choices=TYPE_OF_COMMUNICATIONS,
    )

    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name="communication",
        verbose_name="Контакт",
    )
    pub_date = models.DateTimeField(
        "Дата коммуникации.",
        auto_now_add=True,
    )
