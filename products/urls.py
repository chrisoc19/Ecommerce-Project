from django.conf.urls import url, include
from .views import all_products, all_categories, products_by_category, products_detail


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^category/$', all_categories, name='category'),
    url(r'^(?P<product_slug>[-\w]+)/$', products_detail, name='products_detail'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', products_by_category, name='products_by_category'),
]
