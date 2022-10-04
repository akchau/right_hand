"""Модуль тестирования моделей приложения Contacts
В моделях тестируется корректность метаданных: verbose_name,
help_text и корректность вызова метода __str__ моделей.
"""
from django.test import TestCase

from contacts.models import Contact, Communication, Company


class ContactModelTest(TestCase):
    """Класс тестирования модели Contact."""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.contact = Contact.objects.create(
            name='Имя Тест',
            role='Коллега',
            email='test@test.te',
            frequency_of_communications_days=1,
            date_of_birthday="2000-01-01 00:00:00",
        )

    def test_verbose_name(self):
        """Функция проверки корректности читаемого названия поля."""
        contact = ContactModelTest.contact
        field_verboses = {
            'name': 'Имя контакта',
            'role': 'Роль контакта',
            'email': 'Email',
            'frequency_of_communications_days':
                'Частота коммуникаций. Раз/дней.',
            'date_of_birthday': 'Дата рождения.',
            'company': 'Компания',
            'position': "Должность",
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    contact._meta.get_field(field).verbose_name,
                    expected_value
                )

    def test_help_text(self):
        """"Функция проверки хелп-текста."""
        contact = ContactModelTest.contact
        field_help_text = {
            'name': "Укажите фамилию и имя контакта.",
            'role': "Выберите роль контакта.",
            'email': "Укажите основной email.",
            'frequency_of_communications_days':
                "Укажите как часто хотите общаться с контактом.",
            'date_of_birthday': "Укажите день рождения контакта.",
            'company': "Укажите компанию контакта.",
            'position': "Укажите должность контакта.",
        }
        for field, expected_value in field_help_text.items():
            with self.subTest(field=field):
                self.assertEqual(
                    contact._meta.get_field(field).help_text,
                    expected_value
                )

    def test_object_name_is_name_fild(self):
        """Функция проверки __str__ модели"""
        contact = ContactModelTest.contact
        expected_object_name = contact.name
        self.assertEqual(expected_object_name, str(contact))


class CommunicationModelTest(TestCase):
    """Класс тестирования модели Communication."""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.contact = Contact.objects.create(
            name='Имя Тест',
            role='Коллега',
            email='test@test.te',
            frequency_of_communications_days=1,
            date_of_birthday="2000-01-01 00:00:00",
        )
        cls.communication = Communication.objects.create(
            type='Звонок',
            contact=cls.contact,
        )

    def test_verbose_name(self):
        """Функция проверки корректности читаемого названия поля."""
        communication = CommunicationModelTest.communication
        field_verboses = {
            'type': "Тип коммуникации.",
            'contact': "Контакт",
            'pub_date': "Дата коммуникации.",
            'info': "Описание коммуникации",
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    communication._meta.get_field(field).verbose_name,
                    expected_value
                )

    def test_help_text(self):
        """"Функция проверки хелп-текста."""
        communication = CommunicationModelTest.communication
        field_help_text = {
            'type': "Укажите тип комуникации.",
            'contact': "Укажите контакт коммуникаиции.",
            'pub_date': "Дата контакта.",
            'info': "Добавьте описние",
        }
        for field, expected_value in field_help_text.items():
            with self.subTest(field=field):
                self.assertEqual(
                    communication._meta.get_field(field).help_text,
                    expected_value
                )

    def test_object_name_is_name_fild(self):
        """Функция проверки __str__ модели."""
        contact = CommunicationModelTest.contact
        communication = CommunicationModelTest.communication
        expected_object_name = f"{communication.type} - {contact.name}"
        self.assertEqual(expected_object_name, str(communication))


class PartnerModelTest(TestCase):
    """Класс тестирования модели Company."""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = Company.objects.create(
            inn='12345667',
            legal_adress='улица Пушкина, 21',
            full_name='Рога и Копыта',
            short_name='РиК'
        )

    def test_verbose_name(self):
        """Функция проверки корректности читаемого названия поля."""
        partner = PartnerModelTest.partner
        field_verboses = {
            'inn': "ИНН",
            'kpp': "КПП",
            'ogrn': "ОГРН",
            'okpo': "ОКПО",
            'okved': "ОКВЭД",
            'fact_adress': "Фактический адрес",
            'legal_adress': "Юридический адрес",
            'full_name': "Полное наименование",
            'short_name': "Сокращенное наименование",
            'main_email': "Основной email",
            'phone_number': "Номер телефона",
            'number_acount': "Расчетный счет",
            'cor_acount': "Корреспондентский счет",
            'bic': "БИК",
            'head_of_company': "ФИО руководителя",
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    partner._meta.get_field(field).verbose_name,
                    expected_value
                )

    def test_help_text(self):
        """"Функция проверки хелп-текста."""
        partner = PartnerModelTest.partner
        field_help_text = {
            'inn': "Укажите ИНН.",
            'kpp': "Укажите КПП.",
            'ogrn': "Укажите ОГРН.",
            'okpo': "Укажите ОКПО.",
            'okved': "Укажите ОКВЭД.",
            'fact_adress': "Укажите фактический адрес.",
            'legal_adress': "Укажите юридический адрес.",
            'full_name': "Укажите полное наименование.",
            'short_name': "Укажите сокращенное наименование.",
            'main_email': "Укажите основной email.",
            'phone_number': "Укажите номер телефона.",
            'number_acount': "Укажите номер расчетного счета.",
            'cor_acount': "Укажите номер кореспондентского счета.",
            'bic': "Укажите БИК банка.",
            'head_of_company': "Укажите ФИО руководителя компании.",
        }
        for field, expected_value in field_help_text.items():
            with self.subTest(field=field):
                self.assertEqual(
                    partner._meta.get_field(field).help_text,
                    expected_value
                )

    def test_object_name_is_name_fild(self):
        """Функция проверки __str__ модели."""
        partner = PartnerModelTest.partner
        expected_object_name = partner.short_name
        self.assertEqual(expected_object_name, str(partner))
