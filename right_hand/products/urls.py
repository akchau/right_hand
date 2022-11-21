from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    # Адреса продуктов --------------------------------------------------------
    path('', views.products, name='products'),
    path('<int:pk>/', views.product_profile, name='product_profile'),
    # Адреса сборок --------------------------------------------------------
    path(
        'collections/',
        views.collections,
        name='collections'
    ),
    path(
        'collection/<int:pk>/',
        views.collection_profile,
        name='collection_profile'
    )
]
