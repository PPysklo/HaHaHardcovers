from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def loginUser(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('stuff:stuff-list')
    
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exits')