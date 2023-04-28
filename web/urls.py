from django.urls import path
from .views import *
app_name='web'
urlpatterns=[
    path('',index, name='index'),
    path('search/', search_field, name='search'),
    path('create/', create, name='create'),
]