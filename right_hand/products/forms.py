from django import forms

from .models import Product, Collection


class ProductForm(forms.ModelForm):
    """Форма для создания карточки товара."""
    class Meta:
        model = Product
        fields = (
            "name",
            "reference",
            "maker",
            "price",
            "unit",
        )


class CollectionForm(forms.ModelForm):
    """Форма для создания сборки."""
    class Meta:
        model = Collection
        fields = (
            "name",
            "description",
        )
