from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path("login/", CustomObtainAuthToken.as_view(),name='login'),
    path('verify-email/<str:token>/', VerifyEmailView.as_view(), name='verify-email'),
    path('get-list-user/', get_list_user),
    path('get-user-by-token/<str:token_key>/',get_user_by_token),
    path('update-status/<str:customer_id>/',update_user_status),
    path('get-list-customer/',get_list_customer),
    path('logout/',logout)
]
