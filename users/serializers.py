from rest_framework import serializers
from .models import User, Customer, Admin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_id","full_name","email","username","password","role","phone_number","is_verified")

class AdminSerializerGet(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Admin
        fields = ("admin_id",'user')

class AdminSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ("admin_id",'user')

class CustomerSerializerGet(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = ("customer_id",'user','status')

class CustomerSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("customer_id",'user','status')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'full_name', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            is_verified=False 
        )
        user.role = "Customer" 
        user.save()
        return user