from django.shortcuts import render
from .models import Books
# Create your views here.

def stuffList(request):
    
    books = Books.objects.all()
    
    context = {
        'books' : books
    }
    
    return render(request,'stuff/stuff_list.html', context)
