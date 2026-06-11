from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.display_books, name='books'),
    path('book/<int:book_id>/', views.info_about_book, name='book')
]