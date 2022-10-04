from django.test import TestCase

from contacts.models import Contact


class ContactModelTest(TestCase):
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
