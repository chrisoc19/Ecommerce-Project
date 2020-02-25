from django.test import TestCase
from django.urls import reverse, resolve
from .views import do_search


# Create your tests here.
class Test_urls(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product Urls
    """
    def test_do_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, do_search)
