from django.shortcuts import render, get_object_or_404

from .models import Product, Collection, ProductsCollection


def products(request):
    """Все продукты."""
    template = "products/products.html"
    title = 'Мои продукты.'
    header = title
    products = Product.objects.all().order_by(
        "name")
    context = {
        'title': title,
        'header': header,
        'products': products,
    }
    return render(request, template, context)


def collections(request):
    """Все сборки."""
    template = "products/collections.html"
    title = 'Мои сборки.'
    header = title
    collections = Collection.objects.all().order_by(
        "name")
    context = {
        'title': title,
        'header': header,
        'collections': collections,
    }
    return render(request, template, context)


def product_profile(request, pk):
    """Карточка товара."""
    template = "products/product_profile.html"
    product = get_object_or_404(Product, pk=pk)
    title = 'Карточка товара'
    header = title
    context = {
        'title': title,
        'header': header,
        'product': product,
    }
    return render(request, template, context)


def collection_profile(request, pk):
    """Карточка сборки."""
    template = "products/collection_profile.html"
    collection = get_object_or_404(Collection, pk=pk)
    positions = ProductsCollection.objects.filter(collection=collection)
    title = 'Карточка сборки.'
    header = title
    context = {
        'title': title,
        'header': header,
        'collection': collection,
        'positions': positions,
    }
    return render(request, template, context)
