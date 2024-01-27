from django.urls import path
from . import views

app_name = 'stuff'

urlpatterns = [
    path('',views.stuffList, name='stuff_list'),
    path('book_detail/<str:pk>//', views.DetailBook.as_view(), name="book_detail"),
    path('addBook/', views.addBook, name="add_Book"),
    path('test2/', views.test2View, name="test2"),
    path('navbar/', views.navView, name="nav"),
    
    path('update_book/<str:pk>/', views.updateBook,name='update-book'),
    path('delete-book/<str:pk>/', views.deleteBook,name='delete-book'),
    
    
    
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout,name='checkout'),
    path('update_item/', views.updateitem , name='update-item'),
    path('process_order/', views.processOrder , name='process-order'),
    path('strona1/', views.strona1View,name='s1'),
    path('strona2/', views.strona2View,name='s2'),
    
    
    

]