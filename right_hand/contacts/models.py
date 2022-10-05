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

COMMUNICATOIN_STATUS = [
    ('Выполнена', 'Выполнена'),
    ('Запланирована', 'Запланирована'),
    ('Просрочена', 'Просрочена'),
]


class Company(models.Model):
    """Модель компании."""
    inn = models.CharField(
        "ИНН",
        max_length=10,
        help_text="Укажите ИНН.",
    )
    kpp = models.CharField(
        "КПП",
        max_length=9,
        blank=True,
        null=True,
        help_text="Укажите КПП.",
    )
    ogrn = models.CharField(
        "ОГРН",
        max_length=13,
        blank=True,
        null=True,
        help_text="Укажите ОГРН.",
    )
    okpo = models.CharField(
        "ОКПО",
        max_length=10,
        blank=True,
        null=True,
        help_text="Укажите ОКПО.",
    )
    okved = models.CharField(
        "ОКВЭД",
        max_length=10,
        blank=True,
        null=True,
        help_text="Укажите ОКВЭД.",
    )
    fact_adress = models.TextField(
        "Фактический адрес",
        max_length=10,
        blank=True,
        null=True,
        help_text="Укажите фактический адрес."
    )
    legal_adress = models.TextField(
        "Юридический адрес",
        help_text="Укажите юридический адрес.",
    )
    full_name = models.CharField(
        "Полное наименование",
        max_length=200,
        help_text="Укажите полное наименование.",
    )
    short_name = models.CharField(
        "Сокращенное наименование",
        max_length=150,
        help_text="Укажите сокращенное наименование."
    )
    main_email = models.EmailField(
        "Основной email",
        blank=True,
        null=True,
        help_text="Укажите основной email."
    )
    phone_number = models.CharField(
        "Номер телефона",
        max_length=30,
        blank=True,
        null=True,
        help_text="Укажите номер телефона."
    )
    number_acount = models.CharField(
        "Расчетный счет",
        max_length=20,
        blank=True,
        null=True,
        help_text="Укажите номер расчетного счета."
    )
    cor_acount = models.CharField(
        "Корреспондентский счет",
        max_length=20,
        blank=True,
        null=True,
        help_text="Укажите номер кореспондентского счета."
    )
    bic = models.CharField(
        "БИК",
        max_length=9,
        blank=True,
        null=True,
        help_text="Укажите БИК банка."
    )
    head_of_company = models.CharField(
        "ФИО руководителя",
        max_length=200,
        blank=True,
        null=True,
        help_text="Укажите ФИО руководителя компании."
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
        help_text="Укажите тип комуникации.",
    )

    status = models.CharField(
        "Статус.",
        max_length=20,
        choices=COMMUNICATOIN_STATUS,
        help_text="Укажите статус коммуникации.",
        blank=True,
        null=True,
    )

    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name="communication",
        verbose_name="Контакт",
        help_text="Укажите контакт коммуникаиции."
    )
    pub_date = models.DateTimeField(
        "Дата коммуникации.",
        auto_now_add=True,
        help_text="Дата контакта.",
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
