from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('show_staff/', views.show_staff, name='show_staff'),
    path('show_templeinfo/', views.show_templeinfo, name='temple'),
    path('show_schedule/',views.show_schedule,name='schedule'),
    path('show_special/',views.show_special,name='special'),
    path('show_income/',views.show_income,name='income'),
    path('show_careers/',views.show_careers,name='careers'),
    path('show_darshan/', views.show_darshan, name='darshan'),
    path('search_temple/', views.search_temple, name='searchtemple'),
    path('search_temple1/', views.search_temple1, name='searchtemple1'),
    path('insert_Application/<cid>', views.insert_Application, name='application'),
    path('show_pooja/', views.show_pooja, name='show_pooja'),
    # path('insert_poojabook/<pid>', views.insert_poojabook, name='insert_poojabook'),
    path('Addtocart/<pid>', views.Addtocart, name='addtocart'),
    path('add_addtocart', views.add_addtocart, name='add_addtocart'),
    path('delete_addtocart/<poojaid>', views.delete_addtocart, name='delete_cart'),
    path('Confirm_order/', views.Confirm_order, name='confirm_cart'),

    path('payment/<int:pid>/<int:subtotal>/', views.payment, name='payment'),
    path('index', views.index, name='index'),

]