from django.urls import path
from .views import *
app_name='user'
urlpatterns=[
    path('login/', sign_in , name='login'),
    path('logout/', sign_out, name='logout'),
    path('register/user/', sign_up, name='register'),
]