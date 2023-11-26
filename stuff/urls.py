from django.urls import path
from . import views

app_name = 'stuff'

urlpatterns = [
    path('',views.stuffList, name='stuff-list'),
]