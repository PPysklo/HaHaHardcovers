from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import BookForm

from .models import Books


def test1View(request):
    return render(request, 'bookForm.html')

def test2View(request):
    return render(request, 'test2.html')

def cartView(request):
    return render(request, 'cartForm.html')


def stuffList(request):
    
    books = Books.objects.all()
    
    context = {
        'books' : books
    }
    
    return render(request,'stuff/stuff_list.html', context)
 

    
@login_required(login_url='users:login')
def addBook(request):
    
    form = BookForm()
    
    if request.method == "POST":
       
        form = BookForm(request.POST)

        if form.is_valid():
            book = form.save(commit=False)
            book.save()

            return redirect('stuff:stuff_list')

    context = {'form':form}
    return render(request,'bookForm.html', context=context)