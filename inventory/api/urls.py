from django.urls import path
from .views import AssetListView, AssetDetailView

urlpatterns =[
    path('inventory-list/', AssetListView.as_view(), name='inventory-list' ),
    path('inventory-list/<str:pk>/', AssetDetailView.as_view(), name='inventory-detail' ),
]