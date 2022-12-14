from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    # ----------------------------Адреса продуктов ---------------------------
    path('', views.products, name='products'),
    path('plants/', views.plants_products, name='plants_products'),
    path('new/', views.product_new, name='product_new'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('<int:pk>/', views.product_profile, name='product_profile'),
    # ----------------------------Адреса сборок ------------------------------
    path(
        'collections/',
        views.collections,
        name='collections'
    ),
    path('collection/new/', views.collection_new, name='collection_new'),
    path('collection/<int:pk>/delete/',
         views.collection_delete,
         name='collection_delete'),
    path('collection/<int:pk>/edit/',
         views.collection_edit,
         name='collection_edit'),
    path('collection/<int:pk>/',
         views.collection_profile,
         name='collection_profile'),
    path(
        'collection/<int:pk>/',
        views.collection_profile,
        name='collection_profile'
    )
]
