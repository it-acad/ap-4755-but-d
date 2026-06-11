from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.show_all_orders, name="orders"),
    path('user-orders/', views.show_orders_to_user, name='user-orders'),
    path('add-order/', views.create_order, name='add-order'),
    path('delete-order/<int:order_id>/', views.delete_order, name='delete-order')
]