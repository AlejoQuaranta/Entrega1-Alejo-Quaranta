from django.urls import path
from products.views import Create_product,Update_product, List_products, contacto, search_product_view, create_category_view, create_discount_view, Detail_product, no_hay_error, delete_product

urlpatterns = [
    path('', List_products.as_view(), name = 'list_products'),

    path('contacto/', contacto, name = 'contacto'),
    path('create-product/', Create_product.as_view(), name = 'create_product'),
    path('search-product/', search_product_view, name = 'search_product_view'),
    path('create-category/', create_category_view, name = 'create-category'),
    path('create-discount/', create_discount_view, name = 'create-discount'),
    path('no-hay-error/', no_hay_error, name = 'no-hay-error'),
    path('detail-product/<int:pk>/', Detail_product.as_view(), name = 'detail_product'),
    path('delete-product/<int:pk>/', delete_product, name = 'delete_product'),
    path('update-product/<int:pk>/', Update_product.as_view(), name = 'update_product'),
]


