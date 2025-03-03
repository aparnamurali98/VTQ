from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('view_staff/', views.view_staff, name='update_staff'),
    path('update_staff/<sid>', views.update_staff, name='up_staff'),
    path('incomes', views.incomes, name='insert_incomes'),
    path('view_income', views.view_income, name='view_income'),
    path('view_expense', views.view_expense, name='view_expense'),
    path('pooja_booking/', views.pooja_booking, name='pooja_booking'),
    path("staff_reply/<int:booking_id>/", views.staff_reply, name="reply"),
    path('expense', views.expense, name='insert_expense'),
]