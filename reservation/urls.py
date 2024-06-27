from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path("get-list-reserve-all/",get_list_reserve_all),
    path("get-list-reserve-branch/<str:branch>/",get_list_reserve_branch),
    path("get-list-reserve-customer-history/<str:name>/",get_list_reserve_customer_history),
    path("get-list-reserve-customer/",get_list_reserve_customer),
    path("add-reserve/<str:name>/",add_reserve),
    path("update-reserve/<str:id>/",update_reserve),
    path("done-reserve/<str:id>/",done_reserve)
]