from django.db import models

TYPE_OF_COMMUNICATIONS = [
    ('Звонок', 'Звонок'),
    ('Встреча', 'Встреча'),
    ('Переписка', 'Переписка'),
    ('Видео-звонок', 'Видео-звонок'),
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
        max_length=20,
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
    info = models.TextField(
        "Описание коммуникации",
        help_text="Добавьте описние",
        blank=True,
        null=True,
        default="Нет описания",
    )


class Company(models.Model):
    """Модель компании."""
    inn = models.CharField("ИНН", max_length=10)
    kpp = models.CharField("КПП", max_length=9)
    ogrn = models.CharField("ОГРН", max_length=13)
    okpo = models.CharField("ОКПО", max_length=10, blank=True, null=True)
    okved = models.CharField("ОКВЭД", max_length=10)
    fact_adress = models.TextField()
    legal_adress = models.TextField()
    full_name = models.CharField(
        "Полное наименование",
        max_length=200,
    )
    short_name = models.CharField(
        "Сокращенное наименование",
        max_length=150,
    )
    main_email = models.EmailField("Основной email")
    phone_number = models.CharField("Номер телефона", max_length=30)
    number_acount = models.CharField(
        "Расчетный счет",
        max_length=20,
    )
    cor_acount = models.CharField(
        "Корреспондентский счет",
        max_length=20,
    )
    bic = models.CharField("БИК", max_length=9)
    head_of_company = models.CharField("ФИО руководителя", max_length=200)
