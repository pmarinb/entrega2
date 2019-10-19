from django.urls import path,include
from . import views

urlpatterns=[
    path('login', views.vista_login),
    path('registro', views.registro),
]
