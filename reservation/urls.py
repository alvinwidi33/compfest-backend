from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path("get-list-reserve-feedback/",get_list_reserve_feedback),
    path("get-list-reserve-branch/<str:branch>/",get_list_reserve_branch),
    path("get-list-reserve-customer-history/<str:name>/",get_list_reserve_customer_history),
    path("get-list-reserve-customer/<str:name>/",get_list_reserve_customer),
    path("add-reserve/",add_reserve),
    path("patch-reserve/<str:id>/",patch_reserve)
]
