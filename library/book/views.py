# Create your views here.
from django.shortcuts import redirect, render
from django.contrib import messages
from book.models import Book
# books = Book.get_all()
# return render(request, 'book/books.html', {'books': books})


def display_books(request):
    if not request.user.is_authenticated:
        return redirect('auth:login')

    sort = request.GET.get('sort', 'name')
    allowed_sorting = {
        'name': 'name',
        '-name': '-name',
        'count': 'count',
        '-count': '-count',
        'id': 'id',
        '-id': '-id',
    }

    current_sort = allowed_sorting.get(sort, 'name')
    books = Book.objects.all().order_by(current_sort)

    return render(request, 'book/books.html', {
        'books': books,
        'current_sort': current_sort,
    })

def info_about_book(request, book_id):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    book = Book.get_by_id(book_id)
    if book is None:
        messages.error(request, "Something went wrong and we can't find this book")
        return redirect('book:books')
    
    return render(request, 'book/single-book.html', {'book': book})