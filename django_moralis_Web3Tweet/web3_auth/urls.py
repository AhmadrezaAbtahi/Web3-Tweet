from django.urls import path

from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('transaction_detail', views.transaction_detail, name='transaction_detail')
   ]