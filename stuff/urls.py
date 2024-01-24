from django.urls import path
from . import views

app_name = 'stuff'

urlpatterns = [
    path('',views.stuffList, name='stuff_list'),
    # path('<pk>/', views.BooksDetail.as_view(), name="book_detail"),
    path('addBook/', views.addBook, name="add_Book"),
    path('test2/', views.test2View, name="test2"),
    path('cart/', views.cartView, name='cart')
    

]