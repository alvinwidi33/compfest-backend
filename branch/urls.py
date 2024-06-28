from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns=[
    path('add-branch/',add_branch),
    path('get-list-branch/',get_list_branch),
    path('update-branch/',update_branch),
    path('get-branch-detail/<str:id>/',get_branch_detail)
]
