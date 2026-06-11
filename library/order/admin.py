# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'book_title',
        'user_id',
        'created_at',
        'end_at',
        'plated_end_at'
    ]
    
    search_fields = [
        '=id',
        'book__name',
        'user__id',
        'user__email'
    ]
    
    list_filter = [
        'created_at',
        'plated_end_at',
        'book__name'
    ]
    
    def book_title(self, obj):
        return obj.book.name
    
    book_title.short_description = "Book Title"
    
    def user_id(self, obj):
        return obj.user.id
    
    user_id.short_description = "User ID"
    
    
    
    
admin.site.register(Order, OrderAdmin)