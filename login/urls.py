from django.urls import path

from . import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout)

]