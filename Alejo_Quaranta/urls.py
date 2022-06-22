from django.contrib import admin
from django.urls import path, include
from Alejo_Quaranta.views import fecha_actual, familiares, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fecha_actual/', fecha_actual, name = 'fecha_actual'),
    path('familiares/', familiares, name = 'familiares'),
    path('familia/', include('familia.urls')),
    path('', index, name = 'index'),
    path('products/', include('products.urls')),
]
