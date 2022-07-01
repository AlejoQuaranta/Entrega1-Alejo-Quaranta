from django.urls import path
from products.views import create_product_view, delete_product, List_products, contacto, search_product_view, create_category_view, create_discount_view, Detail_product, no_hay_error, delete_product

urlpatterns = [
    path('', List_products.as_view(), name = 'list_products'),

    path('contacto/', contacto, name = 'contacto'),
    path('create-product/', create_product_view, name = 'create-product'),
    path('search-product/', search_product_view, name = 'search_product_view'),
    path('create-category/', create_category_view, name = 'create-category'),
    path('create-discount/', create_discount_view, name = 'create-discount'),
    path('no-hay-error/', no_hay_error, name = 'no-hay-error'),
    path('detail-product/<int:pk>/', Detail_product.as_view(), name = 'detail-product'),
    path('delete-product/<int:pk>/', delete_product, name = 'delete-product'),
]


