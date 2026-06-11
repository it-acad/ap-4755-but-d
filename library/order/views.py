# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages

from order.models import Order
from authentication.models import CustomUser
from book.models import Book

def show_all_orders(request):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.user.role == 0:
        return redirect('auth:dashboard')
    
    orders = Order.get_all()

    return render(request, 'order/orders.html', {'orders': orders})

def show_orders_to_user(request):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.user.role == 1:
        return redirect('auth:dashboard')
    
    user_id = request.user.id
    
    orders = Order.objects.all()
    
    orders = [o for o in orders if o.user.id == user_id]
    
    return render(request, 'order/orders_for_user.html', {"orders": orders})

def create_order(request):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.user.role == 1:
        return redirect('auth:dashboard')
    
    user_id = request.user.id
    books = Book.get_all()

    user = CustomUser.get_by_id(user_id)
    if request.method == 'POST':
        book_id = request.POST.get('book')
        plated_end_at = request.POST.get('plated_end_at')

        book = Book.get_by_id(book_id)
        if book is None or not plated_end_at:
            messages.error(request, "Invalid data")
            return render(request, 'order/add-order.html', {'books': books})

        order = Order.create(user=user, book=book, plated_end_at=plated_end_at)

        if order is None:
            messages.error(request, "Invalid data")
            return render(request, 'order/add-order.html', {'books': books})
        
        return redirect('order:user-orders')

    return render(request, 'order/add-order.html', {'books': books})

# def delete_author(request, author_id):
#     if not request.user.is_authenticated:
#         return redirect('auth:login')
    
#     if request.user.role == 0:
#         return redirect('auth:dashboard')
    
#     if request.method == 'POST':
#         author = Author.get_by_id(author_id=author_id)
        
#         if author is None:
#             messages.error(request, "Perhaps archives are incomplete. We can't delete what we don't know")
#             return redirect('author:authors')
        
#         deleted = Author.delete_by_id(author_id=author_id)
        
#         if not deleted:
#             messages.error(request, "Something went wrong. The author wasn't deleted")
#             return redirect('author:authors')
        
#         return redirect('author:authors')
    
def delete_order(request, order_id):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.user.role == 0:
        return redirect('auth:dashboard')
    
    if request.method == 'POST':
        order = Order.get_by_id(order_id=order_id)
        
        if order is None:
            messages.error(request, "Perhaps archives are incomplete. We can't delete what we don't know")
            return redirect('order:orders')
        
        deleted = Order.delete_by_id(order_id=order_id)
        
        if not deleted:
            messages.error(request, "Something went wrong. The order wasn't deleted")
            
        return redirect('order:orders')