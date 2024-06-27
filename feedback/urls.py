from django.urls import path
from .views import *

urlpatterns=[
    path("get-feedback-name/<str:name>/",get_feedback_name),
    path("get-feedback-all/",get_list_feedback),
    path("add-feeback/",add_feedback),
    path('get-feedback-branch/<str:branch>/',get_feedback_branch)
]