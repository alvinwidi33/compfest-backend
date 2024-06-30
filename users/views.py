import uuid
import os
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.backends import ModelBackend
from sea_salon import settings 
from .models import User,Customer, Admin
from .serializers import (
    RegisterSerializer, UserSerializer, CustomerSerializerPost, CustomerSerializerGet,
    AdminSerializerPost, AdminSerializerGet)
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth import logout, authenticate
from rest_framework import status, generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.views import APIView
from django.urls import reverse
from.permission import is_admin

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        verification_token = str(uuid.uuid4())

        user.verification_token = verification_token
        user.save()

        customer_data = {
            'user': user.user_id,
            'status': 'Not Member',  
        }
        customer_serializer = CustomerSerializerPost(data=customer_data)
        if customer_serializer.is_valid(raise_exception=True):
            customer_serializer.save()

        subject = 'Verifikasi Akun SEA Salon'
        verification_url = request.build_absolute_uri(
            reverse('verify-email', kwargs={'token': verification_token})
        )
        
        views_dir = os.path.dirname(__file__)
        html_template_path = os.path.join(views_dir, 'email.html')
        
        with open(html_template_path, 'r') as file:
            html_message = file.read()
        
        html_message = render_to_string(html_template_path, {'user': user, 'verification_url': verification_url})
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = user.email

        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

        return Response({
            "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
            "customer": customer_serializer.data,
            "message": "Berhasil Registrasi, silakan buka email Anda untuk verifikasi"
        }, status=status.HTTP_201_CREATED)

class VerifyEmailView(APIView):
    def get(self, request, token, format=None):
        user = get_object_or_404(User, verification_token=token)
        if user.is_verified:
            return Response({'message': 'Akun sudah diverifikasi'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_verified = True
        user.verification_token = None
        user.save()
        return render(request, 'verified.html')
    
class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if '@' in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username_or_email = request.data.get('username_or_email')
        password = request.data.get('password')
        user = EmailOrUsernameModelBackend().authenticate(request, username=username_or_email, password=password)

        if user is not None:
            if not user.is_verified:
                return Response({'error': 'User is not verified.'}, status=status.HTTP_403_FORBIDDEN)
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = UserSerializer(user, many=False)
            return Response({'token': token.key, 'user': user_serializer.data})
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    logout(request)
    return JsonResponse({"message": "Logout successful"})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([is_admin])
def get_list_user(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_by_token(request, token_key):
    try:
        token = Token.objects.get(key=token_key)
        user = token.user

        if user.role == "Customer":
            customer = Customer.objects.get(user=user)
            serializer = CustomerSerializerGet(customer)
        elif user.role == "Admin":
            admin = Admin.objects.get(user=user)
            serializer = AdminSerializerGet(admin)
        else:
            serializer = UserSerializer(user)
            
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Token.DoesNotExist:
        return Response({"error": "User is not logged in"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([is_admin])  
def update_user_status(request, customer_id):
    try:
        customer = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return Response({"message": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CustomerSerializerPost(customer, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    logout(request)
    return JsonResponse({"message": "Logout successful"})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([is_admin])
def get_list_customer(request):
    customers = Customer.objects.all().order_by("user__full_name")
    serializer = CustomerSerializerGet(customers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)