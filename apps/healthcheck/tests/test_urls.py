from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.healthcheck.views import healthcheck
from apps.healthcheck.urls import urlpatterns


class HealthCheckUrlsTestCase(SimpleTestCase):
    def test_healthcheck_url_included_in_urls(self):
        url_names = [url.name for url in urlpatterns]
        self.assertIn("healthcheck", url_names)

    def test_healthcheck_url_resolves(self):
        url = reverse("healthcheck")
        self.assertEqual(resolve(url).func, healthcheck)
