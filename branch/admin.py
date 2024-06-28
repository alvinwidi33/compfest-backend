from django.contrib import admin

from .models import Branch
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    fields=("branch_name","branch_location","image","opening_time","closing_time")
    list_display = ("id","branch_name","branch_location","image","opening_time","closing_time")