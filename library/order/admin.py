# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'book__name',
        'user__id',
        'created_at',
        'end_at',
        'plated_end_at'
    ]
    
    search_fields = [
        'id',
        'book__name',
        'user__id'
    ]
    
    list_filter = [
        'created_at',
        'plated_end_at',
        'book__name'
    ]
    
    
admin.site.register(Order, OrderAdmin)