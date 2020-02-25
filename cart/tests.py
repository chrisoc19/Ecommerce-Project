from django.test import TestCase
from django.urls import reverse, resolve
from .views import view_cart, add_to_cart, adjust_cart, remove_from_cart


# Create your tests here.
class Test_urls(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product Urls
    """
    def test_view_cart_url_is_resolved(self):
        url = reverse('view_cart')
        self.assertEquals(resolve(url).func, view_cart)

    # def test_add_to_cart_url_is_resolved(self):
    #     url = reverse('add_to_cart', args=[str(self.id)])
    #     self.assertEquals(resolve(url).func, 'add_to_cart' )

    # def test_all_adjust_cart_is_resolved(self):
    #     url = reverse('adjust_cart')
    #     self.assertEquals(resolve(url).func, adjust_cart)

    # def test_remove_from_cartl_is_resolved(self):
    #     url = reverse('remove_from_cart', args=['some_slug'])
    #     self.assertEquals(resolve(url).func, remove_from_cart)

    # def test_products_by_category_is_resolved(self):
    #     url = reverse('products_by_category', args=['some_slug'])
    #     self.assertEquals(resolve(url).func, products_by_category)
