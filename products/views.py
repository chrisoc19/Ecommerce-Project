from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# Create your views here.
def product_home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "product_home.html", {"products": products,
                                                 "categories": categories, })


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def products_detail(request, product_slug):
    products = Product.objects.get(slug=product_slug)
    return render(request, "products_detail.html", {"products": products})


def all_categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})


def products_by_category(request, category_slug):
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, "products_by_cat.html", {
                                               "categories": categories,
                                               "products": products,
                                               "category": category})
