from django.urls import path
from .views import CompanyPayableListView, CompanyPayableDetailView, PersonalPayableDetailView,PersonalPayableListView,SchoolPayableDetailView,SchoolPayableListView, AgentPayableListView,AgentPayableDetailView, EmployeePayableListView, EmployeePayableDetailView

urlpatterns =[
    path('company-payable/', CompanyPayableListView.as_view(), name='companyPayable-list' ),
    path('company-payable/<str:pk>/', CompanyPayableDetailView.as_view(), name='companyPayable-detail' ),

    path('personal-payable/', PersonalPayableListView.as_view(), name='personalPayable-list' ),
    path('personal-payable/<str:pk>/', PersonalPayableDetailView.as_view(), name='personalPayable-detail'),

    path('japan-school-payable/', SchoolPayableListView.as_view(), name='schoolPayable-list' ),
    path('japan-school-payable/<str:pk>/', SchoolPayableDetailView.as_view(), name='schoolPayable-detail'),

    path('agent-payable/', AgentPayableListView.as_view(), name='agent-list' ),
    path('agent-payable/<str:pk>/', AgentPayableDetailView.as_view(), name='agent-detail'),

    path('employee-payable/', EmployeePayableListView.as_view(), name='employee-list' ),
    path('employee-payable/<str:pk>/', EmployeePayableDetailView.as_view(), name='employee-detail'),



]