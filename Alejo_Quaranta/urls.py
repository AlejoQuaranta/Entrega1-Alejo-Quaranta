from django.contrib import admin
from django.urls import path, include

from Alejo_Quaranta.views import fecha_actual, familiares, index, login_view, logout_view, register_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fecha_actual/', fecha_actual, name = 'fecha_actual'),
    path('familiares/', familiares, name = 'familiares'),
    path('familia/', include('familia.urls')),
    path('', index, name = 'index'),
    path('products/', include('products.urls')),
    
    
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
