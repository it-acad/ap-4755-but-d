# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'surname',
        'patronymic'
    ]
    
    search_fields = [
        'id',
        'name',
        'surname',
        'patronymic'
    ]
    
    list_filter = [
        'name',
        'surname',
        'patronymic'
    ]
    
    fieldsets = [
        (
            "Info about Author",
            {
                'fields': ('name', 'surname', 'patronymic')
            }
        )
    ]

admin.site.register(Author, AuthorAdmin)