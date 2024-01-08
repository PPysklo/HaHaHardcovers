from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from . import forms

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
            

def captchaTest(request):
    form = forms.FormWithCaptcha()
    context = {"form" : form}
    
    if form.is_valid:
        return render(request,'loginform.html', context)
    
    