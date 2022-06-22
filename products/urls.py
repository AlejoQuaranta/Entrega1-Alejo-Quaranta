from django.urls import path
from products.views import create_product_view, products, contacto, search_product_view, create_category_view, create_discount_view, detail_product, no_hay_error

urlpatterns = [
    path('', products, name = 'products'),
    path('contacto/', contacto, name = 'contacto'),
    path('create-product/', create_product_view, name = 'create-product'),
    path('search-product/', search_product_view, name = 'search_product_view'),
    path('create-category/', create_category_view, name = 'create-category'),
    path('create-discount/', create_discount_view, name = 'create-discount'),
    path('no-hay-error/', no_hay_error, name = 'no-hay-error'),
    path('detail-product/<int:pk>/', detail_product, name = 'detail-product'),
]


