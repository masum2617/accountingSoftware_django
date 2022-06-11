from rest_framework import generics
from services.models import School,Book,BookSale
from .serializers import BookSaleSerializer,SchoolSerializer,BookSerializer

class SchoolListView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
class SchoolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class BookSaleListView(generics.ListCreateAPIView):
    queryset = BookSale.objects.all()
    serializer_class = BookSaleSerializer
    
class BookSaleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookSale.objects.all()
    serializer_class = BookSaleSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer