from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack

class SnackTests(TestCase):
    def test_snack_list_status(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_snack_detail_status(self):
        url = reverse("snack_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_detail_template(self):
        url = reverse("snack_detail", args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_detail.html")
