from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login_Register/',views.loginRegister,name="login_Register"),
    path('logout/',views.logOut, name='logout'),
    
    path('profiles/',  views.profiles, name="profiles"),
    path('profile/<str:pk>/',  views.userProfile, name="user-profile"),
]