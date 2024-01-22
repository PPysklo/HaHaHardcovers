from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView



from .models import Books


def test1View(request):
    return render(request, 'test1.html')

def test2View(request):
    return render(request, 'test2.html')


def stuffList(request):
    
    books = Books.objects.all()
    
    context = {
        'books' : books
    }
    
    return render(request,'stuff/stuff_list.html', context)
 
# class BooksList(ListView):
#     model = Books
    
    
# class BooksDetail(DetailView):
#     model = Books
    

def addBook(request):
    pass
    