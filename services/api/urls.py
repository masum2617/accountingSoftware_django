from django.urls import path
from .views import SchoolDetailView,SchoolListView,BookSaleListView,BookSaleDetailView,BookListView,BookDetailView

urlpatterns =[
    path('schools/', SchoolListView.as_view(), name='school-list' ),
    path('school-detail/<int:pk>/', SchoolDetailView.as_view(), name='school-detail' ),
    
    path('books/', BookListView.as_view(), name='book-list' ),
    path('book-detail/<int:pk>/', BookDetailView.as_view(), name='book-detail' ),

    path('book-sale/', BookSaleListView.as_view(), name='bookSale-list' ),
    path('book-sale-detail/<int:pk>/', BookSaleDetailView.as_view(), name='bookSale-detail' ),

]