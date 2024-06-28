from django.contrib import admin

from users.models import Admin, Customer,User

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    fields = ("user",)
    list_display= ("user_id","user")

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ("user_id","full_name","email","username","password","role","phone_number","is_verified")
    list_display= ("user_id","full_name","email","username","password","role","phone_number","is_verified")

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields=("customer_id",'user','status')
    list_display=("customer_id",'user','status')