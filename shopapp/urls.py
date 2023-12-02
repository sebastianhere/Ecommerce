from shopapp import views
from django.urls import path



urlpatterns=[
    path("",views.Home,name='index'),
    path("about",views.About,name='about'),
    path("news",views.News,name='news'),
    path("shop",views.Shop,name='shop'),
    path("contact",views.Contact,name='contactus'),
    path('cat',views.Categor,name='catpage'),
    path('products/<str:cname>/',views.Productview,name='productviews'),
    path('single/<str:pname>/',views.Singleproduct,name='singleproduct'),
    path("search",views.Searching,name='searchpage'),
    path('cart',views.CartDetails,name='cartpage'),
    path("check",views.Checkout,name='checkout'),
    path('add_cart/<int:product_id>/',views.add_cart,name='add_cart'),
    path('cart_decrement/<int:product_id>', views.min_cart, name='cart_decrement'),
    path('remove/<int:product_id>', views.delete_cart, name='remove'),
]