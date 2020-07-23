
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('webyh/', views.yellowlab),
    path('yellowlab_test/', views.yellowlab_test),
    path('caseapi/', views.caseapi_index),
    path('caseadd/', views.case_add),
    path('casetest/',views.case_test),
    path('casesave/',views.case_save),
    path('testlist_index/',views.testlist_index),
    path('case_edit/',views.case_edit),
    path('case_update/',views.case_update),
    path('case_report/',views.case_report),
    path('case_report_index/',views.case_report_index),
    path('searchcase/',views.searchcase),
    path('searchreport/',views.searchreport)
]