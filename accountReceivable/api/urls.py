from django.urls import path
from .views import CompanyReceivableListView,CompanyReceivableDetailView, PersonalReceivableDetailView,PersonalReceivableListView, SchoolReceivableDetailView,SchoolReceivableListView, StudentlReceivableListView,StudentReceivableDetailView

urlpatterns =[
    path('company/', CompanyReceivableListView.as_view(), name='companyReceivable-list' ),
    path('company/<str:pk>/', CompanyReceivableDetailView.as_view(), name='companyReceivable-detail'),

    path('personal/', PersonalReceivableListView.as_view(), name='personalReceivable-list' ),
    path('personal/<str:pk>/', PersonalReceivableDetailView.as_view(), name='personalReceivable-detail' ),

    path('japan-school/', SchoolReceivableListView.as_view(), name='school-list' ),
    path('japan-school/<str:pk>/', SchoolReceivableDetailView.as_view(), name='school-detail' ),

    path('student-receivable/', StudentlReceivableListView.as_view(), name='student-receivable-list' ),
    path('student-receivable/<str:pk>/', StudentReceivableDetailView.as_view(), name='student-receivable-detail' ),
]