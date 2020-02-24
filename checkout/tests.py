from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import checkout


# Create your tests here.
class Test_urls(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product Urls
    """
    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)


