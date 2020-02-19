from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator


# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    paginator = Paginator(products, 100)
    items = paginator.page(paginator.num_pages)
    return render(request, "product_home.html", {"products": products,
                                                 "items": items})
