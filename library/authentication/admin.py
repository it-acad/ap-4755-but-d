# Register your models here.
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'first_name',
        'middle_name',
        'last_name',
        'role',
        'is_active',
        'is_staff',
        'is_superuser',
        'created_at'
        ]
    
    list_filter = [
        'role',
        'is_active'
    ]
    
    search_fields = [
        'id',
        'email',
        'first_name',
        'middle_name',
        'last_name'
    ]
    
    
admin.site.register(CustomUser, CustomUserAdmin)