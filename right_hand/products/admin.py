from django.contrib import admin

from .models import Product, Collection, ProductsCollection


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'numbers_of_position_in',
        'total_of_position_in'
    )
    empty_value_display = "-пусто-"


class ProductsCollectionAdmin(admin.ModelAdmin):
    list_display = (
        'collection',
        'product',
        'numbers',
        'price_of_position',
        'total_of_position',
    )
    list_editable = (
        'product',
        'numbers',
    )

    empty_value_display = "-пусто-"


admin.site.register(Product)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(ProductsCollection, ProductsCollectionAdmin)
