from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from django.shortcuts import get_object_or_404

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import BookForm
from .utils import searchProject, paginateProjects
from .models import Books, Order, OrderItem, ShippingAddress, Tag


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
    # books = Books.objects.all()
    books, search_query = searchProject(request)
    print(request.GET)
    tags = Tag.objects.all()
    if request.GET.get('category'):
        category_name = request.GET['category']
        
        # Get the tag object corresponding to the category name
        category_tag = get_object_or_404(Tag, name=category_name)

        # Filter books that have the specified tag
        books = books.filter(tags=category_tag)
        print(books)
   
  
    custom_range, books = paginateProjects(request, books, 3)
    
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0, 'shipping': True}
        cartItems = order['get_cart_items']
        
    
    context = {
        'books' : books,
        'tags' : tags,
        'cartitems' : cartItems,
        'search_query' : search_query,
        'custom_range' : custom_range,
    }
    
    return render(request,'stuff/stuff_list.html', context)
 

    
@user_passes_test(lambda u: u.is_superuser, login_url='stuff:stuff_list')
def addBook(request):

    form = BookForm()
    
    if request.method == "POST":
        tag = request.POST.get('tags')

        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            
            tag, created = Tag.objects.get_or_create(id=tag)
            book.tags.add(tag)
            
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

@user_passes_test(lambda u: u.is_superuser, login_url='stuff:stuff_list')
def deleteBook(request,pk):
    print(pk)
    book = Books.objects.get(id=pk)
    
    if request.method == 'POST':
        book.delete()
        return redirect('stuff:stuff_list')

    context = {
    'object' : book
    }
    return render(request,'delete_template.html',context=context)

class DetailBook(DetailView):
    model = Books


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