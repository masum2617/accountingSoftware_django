from services.models import Book,BookSale,School
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSale
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'