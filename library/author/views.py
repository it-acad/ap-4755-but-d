# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from author.models import Author
from book.models import Book

def show_all_authors(request):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.user.role == 0:
        return redirect('auth:dashboard')
    
    authors = Author.get_all()

    return render(request, 'author/authors.html', {'authors': authors})

def add_author(request):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.user.role == 0:
        return redirect('auth:dashboard')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        if name:
            name = name.strip()
        if surname:
            surname = surname.strip()
        if patronymic:
            patronymic = patronymic.strip()
        
        author = Author.create(name=name, surname=surname, patronymic=patronymic)
        
        if author is None:
            messages.error(request, "Invalid data")
            return redirect('author:add-author')
        
        return redirect('author:authors')
    
    return render(request, 'author/add-author.html')

def delete_author(request, author_id):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.user.role == 0:
        return redirect('auth:dashboard')
    
    if request.method == 'POST':
        books = Book.objects.all()
        authors_ids = set([author.id for book in books for author in book.authors.all()])
        author = Author.get_by_id(author_id=author_id)

        if author is None:
            messages.error(request, "Perhaps archives are incomplete. We can't delete what we don't know")
            return redirect('author:authors')

        if author.id not in authors_ids:
            deleted = Author.delete_by_id(author_id=author_id)
        
            if not deleted:
                messages.error(request, "Something went wrong. The author wasn't deleted")
                return redirect('author:authors')
        
            return redirect('author:authors')
        else:
            messages.error(request, "Can't delete this author")
            return redirect('author:authors')
    
    return redirect('author:authors') 