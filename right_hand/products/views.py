from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
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


def product_delete(request, pk):
    Product.objects.get(pk=pk).delete()
    return redirect("products:products")


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(
        request.POST or None,
        files=request.FILES or None,
        instance=product,
    )
    if form.is_valid():
        form.save()
        return redirect("products:product_profile", pk=pk)
    title = "Редактирование товара"
    header = title
    action = "Редактируйте товар"
    template = "products/product_new.html"
    context = {
        "title": title,
        "header": header,
        "action": action,
        "form": form,
        "is_edit": True,
        "pk": pk,
    }
    return render(request, template, context)


def product_new(request):
    """Добавление нового товара."""
    form = ProductForm(
        request.POST or None,
    )
    if form.is_valid():
        form.save()
        return redirect("products:products")
    template = "products/product_new.html"
    title = "Новый товар."
    action = "Добавьте новый товар."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
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
