from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView



from .models import Books

def stuffList(request):
    
    books = Books.objects.all()
    
    context = {
        'books' : books
    }
    
    return render(request,'stuff/stuff_list.html', context)
 
# class BooksList(ListView):
#     model = Books
    
    
class BooksDetail(DetailView):
    model = Books
    

def addBook(request):
    pass
    