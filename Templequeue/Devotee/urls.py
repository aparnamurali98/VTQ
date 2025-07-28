from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='dev_home'),
    path('show_staff/', views.show_staff, name='show_staff'),
    path('show_templeinfo/', views.show_templeinfo, name='temple'),
    path('show_priest/', views.show_priest, name='priest'),
    path('show_schedule/<int:temple_id>',views.show_schedule,name='Schedule'),
    path('show_special/',views.show_special,name='Special'),
    path('show_income/',views.show_income,name='Income'),
    path('show_careers/',views.show_careers,name='showcareers'),
    path('show_darshan/<int:temple_id>', views.show_darshan, name='Darshan'),
    path('search_temple/', views.search_temple, name='searchtemple'),
    path('search_temple1/', views.search_temple1, name='searchtemple1'),
    path('insert_Application/<cid>', views.insert_Application, name='application'),
    path('show_pooja/<int:id>/', views.show_pooja, name='show_pooja'),
    path('Addtocart/', views.Addtocart, name='addtocart'),
    path('add_addtocart', views.add_addtocart, name='add_addtocart'),
    path('delete_addtocart/<poojaid>', views.delete_addtocart, name='delete_cart'),
    path('Confirm_order/', views.Confirm_order, name='confirm_cart'),
    path('payment/<int:pid>/<int:subtotal>/', views.payment, name='payment'),
    path('index', views.index, name='index'),
    path('receipt/<int:pid>/', views.receipt, name='receipt'),
    path('show_receipt/',views.show_receipt,name='receiptview'),


]