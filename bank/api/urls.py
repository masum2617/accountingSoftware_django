from django.urls import path
from bank.api.views import BankListView, BankListDetailView, StatementDetailView, StatementListView

urlpatterns = [

    path('bank-list/', BankListView.as_view(), name='banks-list'),
    path('bank-list/<int:pk>/', BankListDetailView.as_view(), name='banks-detail'),

    path('statements/', StatementListView.as_view(), name='statements'),
    path('statement-detail/<int:pk>/', StatementDetailView.as_view(), name='statement-detail'),
   
] 
