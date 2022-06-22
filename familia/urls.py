from django.urls import path

from familia.views import family

urlpatterns =[
    path('', family, name = 'familia'),
]