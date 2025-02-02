from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('insert_devotee',views.insert_devotee,name='devotee'),
    path('insert_enquiry', views.insert_enquiry, name='enquiry'),
    path('login',views.login,name='login'),



]