from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Product


class DashboardLanguageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.staff = get_user_model().objects.create_user(username="warehouse", is_staff=True)
        Product.objects.create(sku="ABC-123", name="Warehouse Widget", opening_stock=3)

    def test_each_language_switches_the_dashboard(self):
        self.client.force_login(self.staff)
        dashboard = reverse("dashboard")

        for code, _ in settings.LANGUAGES:
            with self.subTest(language=code):
                page = self.client.post(
                    reverse("set_language"), {"language": code, "next": dashboard}, follow=True
                )
                self.assertRedirects(page, dashboard)
                self.assertEqual(page.headers["Content-Language"], code)
                self.assertContains(page, "ABC-123")
                self.assertContains(page, "Warehouse Widget")
                if code != "en":
                    self.assertNotContains(page, "ERP Management System")

    def test_translates_stock_status_and_sets_rtl_direction(self):
        self.client.force_login(self.staff)
        switch = reverse("set_language")
        dashboard = reverse("dashboard")

        page = self.client.post(switch, {"language": "ta", "next": dashboard}, follow=True)
        self.assertContains(page, "குறைந்த இருப்பு")

        page = self.client.post(switch, {"language": "ar", "next": dashboard}, follow=True)
        self.assertContains(page, '<html lang="ar" dir="rtl">')

        page = self.client.post(switch, {"language": "en", "next": dashboard}, follow=True)
        self.assertContains(page, '<html lang="en" dir="ltr">')
        self.assertContains(page, "Low Stock")
