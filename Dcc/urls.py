
from django.urls import path

from . import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('webyh/', views.yellowlab),
    path('yellowlab_test/', views.yellowlab_test)

]