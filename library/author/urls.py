from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('', views.show_all_authors, name='authors'),
    path('add-author/', views.add_author, name='add-author'),
    path('delete-author/<int:author_id>/', views.delete_author, name='delete-author')
]