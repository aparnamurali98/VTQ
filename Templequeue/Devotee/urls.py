

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

]