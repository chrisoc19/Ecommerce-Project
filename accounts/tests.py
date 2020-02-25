from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import logout, login, registration


# Create your tests here.
class Test_urls(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product Urls
    """
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_register_url_is_resolved(self):
        url = reverse('registration')
        self.assertEquals(resolve(url).func, registration)


class Test_views(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product views
    """
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.registration_url = reverse('registration')
        self.logout_url = reverse('products')

    def test_registration(self):
        response = self.client.get(self.registration_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html', 'base.html')

    def test_login(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html', 'base.html')

    def test_logout(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html', 'base.html')
