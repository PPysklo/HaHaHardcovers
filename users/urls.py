from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/',views.loginUser,name="login"),
    path('register/',views.registerUser, name='register'),
    path('logout/',views.logOut, name='logout'),
    
    path('profiles/',  views.profiles, name="profiles"),
    path('profile/<str:pk>/',  views.userProfile, name="user-profile"),
]