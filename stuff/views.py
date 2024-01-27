from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import BookForm

from .models import Books, Order, OrderItem, ShippingAddress


def test1View(request):
    return render(request, 'bookForm.html')

def test2View(request):
    return render(request, 'test2.html')

def cartView(request):
    return render(request, 'cart.html')

def navView(request):
    return render(request, 'stuff/navbar.html')

def strona1View(request):
    return render(request, 'strona1.html')

def strona2View(request):
    return render(request, 'strona2.html')

def stuffList(request):
    
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0, 'shipping': True}
        cartItems = order['get_cart_items']
        
    books = Books.objects.all()
    
    context = {
        'books' : books,
        'cartitems' : cartItems,
    }
    
    return render(request,'stuff/stuff_list.html', context)
 

    
@user_passes_test(lambda u: u.is_superuser, login_url='stuff:stuff_list')
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

@user_passes_test(lambda u: u.is_superuser, login_url='stuff:stuff_list')
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

@csrf_exempt  
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0, 'shipping': True}
        
    context = {'items':items, 'order': order}
    return render(request, 'stuff/checkout.html', context)

  
def updateitem(request):
    data = json.loads(request.body)
    productId = data['bookId']
    action = data['action']
    print(productId)
    print(action)
    
    
    customer = request.user.profile
    book = Books.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, book = book)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
         orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        
        if total == order.get_cart_total:
            order.complete = True
        order.save()
        
        
        if order.shipping == True:
            ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
		)
        
    else:
        print("User is not logged in ")
    
    
    return JsonResponse("Pyment submitted", safe=False)