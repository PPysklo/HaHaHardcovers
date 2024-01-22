from django.urls import path
from . import views

app_name = 'stuff'

urlpatterns = [
    path('',views.stuffList, name='stuff_list'),
    path('<pk>/', views.BooksDetail.as_view, name="book_detail"),
]