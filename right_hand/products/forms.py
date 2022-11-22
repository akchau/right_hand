from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    """Форма для создания контакта."""
    class Meta:
        model = Product
        fields = (
            "name",
            "reference",
            "maker",
            "price",
            "unit",
        )
