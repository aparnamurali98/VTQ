from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('view_staff/', views.view_staff, name='update_staff'),
    path('update_staff/<sid>', views.update_staff, name='up_staff'),
    path('incomes', views.incomes, name='insert_incomes'),
    path('view_income', views.view_income, name='view_income'),

]