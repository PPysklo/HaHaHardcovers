from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import BookForm

from .models import Books, Order


def test1View(request):
    return render(request, 'bookForm.html')

def test2View(request):
    return render(request, 'test2.html')

def cartView(request):
    return render(request, 'cart.html')

def navView(request):
    return render(request, 'navbar.html')


def stuffList(request):
    
    books = Books.objects.all()
    
    context = {
        'books' : books
    }
    
    return render(request,'stuff/stuff_list.html', context)
 

    
@login_required(login_url='users:login_Register')
def addBook(request):
    
    form = BookForm()
    
    if request.method == "POST":
       
        form = BookForm(request.POST)

        if form.is_valid():
            book = form.save(commit=False)
            book.save()

            return redirect('stuff:stuff_list')

    context = {'form':form}
    return render(request,'stuff/add_book.html', context=context)

@login_required(login_url='users:login_Register')
def updateBook(request, pk):
    book = Books.objects.get(id=pk)

    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance = book)

    
        if form.is_valid():
            book = form.save()
    
        return redirect('stuff:stuff_list')
    
    context = {'form': form ,'book': book}
    return render(request, 'stuff/update_book.html', context )

def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0}
        
    context = {'items':items, 'order': order}
    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0}
        
    context = {'items':items, 'order': order}
    return render(request, 'stuff/checkout.html', context)
    