from django.urls import path
from .views import CompanyPayableListView, CompanyPayableDetailView

urlpatterns =[
    path('', CompanyPayableListView.as_view(), name='accountPayable-list' ),
    path('<int:pk>/', CompanyPayableDetailView.as_view(), name='accountPayable-detail' ),
]