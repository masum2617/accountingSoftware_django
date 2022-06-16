from django.urls import path
from .views import EmployeeListView,EmployeeDetailView

urlpatterns =[
    path('employee-list/', EmployeeListView.as_view(), name='employee-list' ),
    path('employee-detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail' ),
]