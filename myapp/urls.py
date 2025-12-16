from django.urls import path 
from .views import index,about,blog,contact,services,login_view,logout,register,icecream,cart,add_to_cart,place_order
urlpatterns = [ 
 
path('',index,name='index'), 
 
path('about/',about,name='about'), 
 
path('blog/',blog,name='blog'), 
 
path('icecream/',icecream,name='icecream'), 
 
path('contact/',contact,name='contact'), 
 
path('services/',services,name='services'), 
 

path('login/',login_view,name='login'),
path('logout/',logout,name='logout'),
path('register/',register,name='register'),
path('cart/',cart,name='cart'),
path('add_to_cart/<int:pid>/', add_to_cart, name='add_to_cart'),
path('place_order/',place_order, name='place_order'),


]
