from django.test import SimpleTestCase, Client
from django.urls import reverse


class HealthCheckTestCase(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_healthcheck_view(self):
        url = reverse("healthcheck")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
