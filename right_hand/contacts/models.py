from datetime import datetime

from django.db import models

from . import validators


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
    ('Выполнено', 'Выполнено'),
    ('Запланировано', 'Запланировано'),
]


class Company(models.Model):
    """Модель компании."""
    inn = models.CharField(
        "ИНН",
        max_length=12,
        blank=True,
        null=True,
        help_text="Укажите ИНН. Для Юр.лица - 10 цифр,для Физ.лица - 12",
        validators=[validators.validate_inn]
    )
    kpp = models.CharField(
        "КПП",
        max_length=9,
        blank=True,
        null=True,
        help_text="Укажите КПП. Состоит из 9 цифр",
        validators=[validators.validate_kpp]
    )
    ogrn = models.CharField(
        "ОГРН",
        max_length=13,
        blank=True,
        null=True,
        help_text="Укажите ОГРН. Состоит из 13 цифр",
    )
    okpo = models.CharField(
        "ОКПО",
        max_length=10,
        blank=True,
        null=True,
        help_text=(
            'Укажите ОКПО. Для Юр.лица - 8 цифр, '
            'для Физ.лица(ИП) - 10 цифр'
        ),
        validators=[validators.validate_okpo]
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
        blank=True,
        null=True,
        help_text="Укажите фактический адрес."
    )
    legal_adress = models.TextField(
        "Юридический адрес",
        help_text="Укажите юридический адрес.",
        blank=True,
        null=True,
    )
    full_name = models.CharField(
        "Полное наименование",
        max_length=200,
        help_text="Укажите полное наименование.",
        blank=True,
        null=True,
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
    mobile_number_of_head = models.CharField(
        "Мобильный телефон директора",
        max_length=30,
        blank=True,
        null=True,
        help_text="Укажите номер телефона.",
        validators=[validators.validate_mobile_phone_number]
    )

    def __str__(self):
        return self.short_name

    def save(self, *args, **kwargs):
        if self.mobile_number_of_head:
            self.mobile_number_of_head = self.mobile_number_of_head.strip()
            elements = [
                '+',
                '-',
                ' ',
                ')',
                '(',
            ]
            for element in elements:
                self.mobile_number_of_head = self.mobile_number_of_head.replace(
                    element,
                    ''
                )
            len_number = len(self.mobile_number_of_head)
            if len_number == 10:
                self.mobile_number_of_head = f'7{self.mobile_number_of_head}'
            self.mobile_number_of_head = (
                f'+7({self.mobile_number_of_head[1:4]}) '
                f'{self.mobile_number_of_head[4:7]}-'
                f'{self.mobile_number_of_head[7:9]}-'
                f'{self.mobile_number_of_head[9:11]}'
            )
        super().save(*args, **kwargs)


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
    mobile_phone_number = models.CharField(
        "Мобильный телефон",
        max_length=30,
        blank=True,
        null=True,
        help_text="Укажите номер телефона.",
        validators=[validators.validate_mobile_phone_number]
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
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.strip().lower()
            elements = [
                '+',
                ')',
                '(',
                '*',
                '?',
            ]
            numbers_all = [str(x) for x in range(10)]
            for element in elements:
                self.name = self.name.replace(element, '')
            for number in numbers_all:
                self.name = self.name.replace(number, '')
            self.name = self.name.title()
        if self.mobile_phone_number:
            self.mobile_phone_number = self.mobile_phone_number.strip()
            elements.append('-')
            for element in elements:
                self.mobile_phone_number = self.mobile_phone_number.replace(
                    element,
                    ''
                )
            len_number = len(self.mobile_phone_number)
            if len_number == 10:
                self.mobile_phone_number = f'7{self.mobile_phone_number}'
            self.mobile_phone_number = (f'+7({self.mobile_phone_number[1:4]}) '
                                        f'{self.mobile_phone_number[4:7]}-'
                                        f'{self.mobile_phone_number[7:9]}-'
                                        f'{self.mobile_phone_number[9:11]}')
        super().save(*args, **kwargs)


class Communication(models.Model):
    """Модель коммуникации."""

    type = models.CharField(
        "Тип",
        max_length=20,
        choices=TYPE_OF_COMMUNICATIONS,
        help_text="Укажите тип",
    )

    status = models.CharField(
        "Статус",
        max_length=20,
        choices=COMMUNICATOIN_STATUS,
        help_text="Укажите статус",
        blank=True,
        null=True,
    )

    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name="communication",
        verbose_name="Контакт",
        help_text="Укажите контакт"
    )
    pub_date = models.DateTimeField(
        "Дата создания",
        auto_now_add=True,
        help_text="Укажите дату создания",
    )
    plan_date = models.DateTimeField(
        "Планируемая дата",
        help_text="Укажите планируемую дату",
        blank=True,
        null=True,
    )
    done_date = models.DateTimeField(
        "Дата",
        help_text="Укажите дату",
        blank=True,
        null=True,
    )
    info = models.TextField(
        "Описание",
        help_text="Добавьте описание",
        blank=True,
        null=True,
        default="Добавьие описание",
    )

    @property
    def is_expired(self):
        if self.status == "Запланировано":
            datetime.today().timestamp() > self.plan_date.timestamp()
            return True
        return False

    def __str__(self):
        return f"{self.type} - {self.contact} - {self.plan_date}"
