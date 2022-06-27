from django.urls import path
from .views import EmployeeListView,EmployeeDetailView, AgentListView, AgentDetailView

urlpatterns =[
    path('employee-list/', EmployeeListView.as_view(), name='employee-list' ),
    path('employee-detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail' ),
    path('agent-list/', AgentListView.as_view(), name='agent-list' ),
    path('agent-detail/<int:pk>/', AgentDetailView.as_view(), name='agent-detail' ),
]