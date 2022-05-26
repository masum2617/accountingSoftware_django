from django.urls import path
from bank.api.views import BankListView, BankListDetailView

urlpatterns = [

    path('bank-list/', BankListView.as_view(), name='banks-list'),
    path('bank-list/<int:pk>/', BankListDetailView.as_view(), name='banks-list'),

   
] 
