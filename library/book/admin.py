# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'count',
        'authors_list'
    ]
    
    list_filter = [
        'count',
        'authors'
    ]
    
    search_fields = [
        '=id',
        'name',
        '=count',
        'authors__name',
        'authors__surname'
    ]
    
    fieldsets = [
        (
            "Static info about book",
            {'fields':('name','description', 'authors')}
        ),
        (
            "Info that can be changed",
            {'fields':('count',)}
        )
    ]
    
    def authors_list(self, obj):
        return ", ".join(
            f"{author.name} {author.surname}"
            for author in obj.authors.all()
        )
        
    authors_list.short_description = "Authors"
    
    
admin.site.register(Book, BookAdmin)