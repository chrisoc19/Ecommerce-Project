from django.test import TestCase
from django.urls import reverse, resolve
from .forms import MakePaymentForm
from .views import checkout, OrderForm


# Create your tests here.
class Checkoutests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Checkout model
    """

    def setUp(self):
        self.product1 = Product.objects.create(
            full_name='john smith',
            phone_number='12345678',
            country='sweden',
            postcode='12345',
            town_or_city='johnvill',
            street_address1='somewhere',
            street_address2='sweden',
            county='kerry',
            date='25/01/2021'
        )
   
class Test_urls(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product Urls
    """
    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)


class TestForm(TestCase):

    def test_blank_data(self):
        form = MakePaymentForm({},)
        self.assertFalse(form.is_valid())

    def test_payment_data(self):
        form = MakePaymentForm({
            'MONTH_CHOICES': "12",
            'YEAR_CHOICES': "2021",
            'credit_card_number': "5555 5555 5555 4444",
            'cvv': "123",
            'expiry_month': "10",
            'stripe_id': "344",
        })
        self.assertTrue(form.is_valid())

    def test_OrderForm_blank_data(self):
        form = OrderForm({},)
        self.assertFalse(form.is_valid())

    def test_OrderForm_data(self):
        form = OrderForm({
            'full_name': "chris oc",
            'phone_number': "2021",
            'postcode': "5555",
            'town_or_city': "killarney",
            'street_address1': "flogsat",
            'street_address2': "poop",
            'country': 'country'
        })
        self.assertTrue(form.is_valid())
