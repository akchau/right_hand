from http import HTTPStatus
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from ..models import Contact, Communication, Company

User = get_user_model()


class ContactsURLTests(TestCase):
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
        cls.partner = Company.objects.create(
            inn='12345667',
            legal_adress='улица Пушкина, 21',
            full_name='Рога и Копыта',
            short_name='РиК'
        )

    def setUp(self):
        self.guest_client = Client()

    def adress_dict(self):
        urls_templates_dict = {
            "/contacts/": "contacts/contacts.html",
            f"/contacts/{self.contact.pk}/": "contacts/contact_profile.html",
            f"/contacts/new_with_partner/{self.partner.pk}/":
                "contacts/contact_new.html",
            "/contacts/new/": "contacts/contact_new.html",
            f"/contacts/{self.contact.pk}/edit/": "contacts/contact_new.html",

            "/contacts/communications/": "contacts/communications.html",
            "/contacts/communication/new/": "contacts/communication_new.html",
            f"/contacts/communication/new_with/{self.contact.pk}/":
                "contacts/communication_new_with.html",
            f"/contacts/communication/{self.communication.pk}/":
                "contacts/communication_profile.html",
            f"/contacts/communication/{self.communication.pk}/edit/":
                "contacts/communication_new.html",

            "/contacts/partners/": "contacts/partners.html",
            "/contacts/partner/new/": "contacts/partner_new.html",
            f"/contacts/partner/{self.partner.pk}/":
                "contacts/partner_profile.html",
            f"/contacts/partner/{self.partner.pk}/edit/":
                "contacts/partner_new.html",
        }
        return urls_templates_dict

    def test_urls_uses_correct_templates(self):
        self.templates_url_names = self.adress_dict()
        for adress, template in self.templates_url_names.items():
            with self.subTest(adress=adress):
                response = self.guest_client.get(adress)
                self.assertTemplateUsed(response, template)

    def test_url_exist_at_desired_location(self):
        url_names = self.adress_dict().keys()
        for adress in url_names:
            with self.subTest(adress=adress):
                response = self.guest_client.get(adress)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_no_exist_return_404(self):
        response = self.guest_client.get("/unexisting/")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
