from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("",views.index, name = 'home'),
    path("home/",views.index, name = 'home'),
    path("about",views.about,name = 'about'),
    path("vehicles/", views.vehicles, name= "vehicles"),
    path("register", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("signout",views.signout,name = "signout"),
    path("bill",views.order,name = "bill"),
    path("contact/",views.contact,name = 'contact'),
    path("orders/",views.getOrder,name = 'orders'),
    path('orders/', views.getOrder, name='getOrder'),  # Ensure this exists
    path('delete_order/<str:order_id>/', views.delete_order, name='delete_order'),
    # path("vehicles",views.Order,name = 'vehicles'),
    # path("bike",views.bike,name = 'bike'),
    # path("bus",views.bus,name = 'bus'),
    
    # path("bill", views.bill, name="bill"),

    ]