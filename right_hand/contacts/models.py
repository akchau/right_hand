from django.db import models

TYPE_OF_COMMUNICATIONS = [
    ('Звонок', 'Звонок'),
    ('Встреча', 'Встреча'),
    ('Переписка', 'Переписка'),
    ('Видео-звонок', 'Видео-звонок'),
]
CONTACT_ROLE = [
    ('Член семьи', 'Член семьи'),
    ('Подчиненый', 'Подчиненый'),
    ('Товарищ', 'Товарищ'),
    ('Коллега', 'Коллега'),
    ('Деловой партнер', 'Деловой партнер'),
]


class Company(models.Model):
    """Модель компании."""
    inn = models.CharField("ИНН", max_length=10)
    kpp = models.CharField("КПП", max_length=9, blank=True, null=True)
    ogrn = models.CharField("ОГРН", max_length=13, blank=True, null=True)
    okpo = models.CharField("ОКПО", max_length=10, blank=True, null=True)
    okved = models.CharField("ОКВЭД", max_length=10, blank=True, null=True)
    fact_adress = models.TextField(max_length=10, blank=True, null=True)
    legal_adress = models.TextField()
    full_name = models.CharField(
        "Полное наименование",
        max_length=200,
    )
    short_name = models.CharField(
        "Сокращенное наименование",
        max_length=150,
        blank=True,
        null=True,
    )
    main_email = models.EmailField("Основной email", blank=True, null=True)
    phone_number = models.CharField(
        "Номер телефона",
        max_length=30,
        blank=True,
        null=True
    )
    number_acount = models.CharField(
        "Расчетный счет",
        max_length=20,
        blank=True,
        null=True,
    )
    cor_acount = models.CharField(
        "Корреспондентский счет",
        max_length=20,
        blank=True,
        null=True,
    )
    bic = models.CharField(
        "БИК",
        max_length=9,
        blank=True,
        null=True,
    )
    head_of_company = models.CharField(
        "ФИО руководителя",
        max_length=200,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.short_name


class Contact(models.Model):
    """Модель контакта."""

    name = models.CharField(
        "Имя контакта",
        max_length=200,
        help_text="Укажите фамилию и имя контакта.",
    )
    role = models.CharField(
        "Роль контакта",
        help_text="Выберите роль контакта.",
        max_length=20,
        blank=True,
        null=True,
        choices=CONTACT_ROLE,
    )
    email = models.EmailField(
        "Email",
        blank=True,
        null=True,
        help_text="Укажите основной email.",
    )
    frequency_of_communications_days = models.IntegerField(
        "Частота коммуникаций. Раз/дней.",
        help_text="Укажите как часто хотите общаться с контактом.",
    )
    date_of_birthday = models.DateTimeField(
        "Дата рождения.",
        blank=True,
        null=True,
        help_text="Укажите день рождения контакта.",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        related_name="company",
        verbose_name="Компания",
        null=True,
        blank=True,
        help_text="Укажите компанию контакта.",
    )
    position = models.CharField(
        "Должность",
        max_length=200,
        help_text="Укажите должность контакта.",
    )

    def __str__(self):
        return self.name


class Communication(models.Model):
    """Модель коммуникации."""

    type = models.CharField(
        "Тип коммуникации.",
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

    def __str__(self):
        return f"{self.type} - {self.contact}"
