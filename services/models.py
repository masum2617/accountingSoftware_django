from django.db import models
from student.models import Student
# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=50)
    school_address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.school_name

class Book(models.Model):
    book_name = models.CharField(max_length=80)
    book_price = models.CharField(max_length=80, null=True, blank=True)
    purchase_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    book_stock_quantity = models.IntegerField(null=True, blank=True)
    book_image= models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return self.book_name

class BookSale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    sold_quantity = models.IntegerField(null=True, blank=True)
    sold_to_student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    sold_to_other =  models.CharField(max_length=80, null=True, blank=True)
    price_of_each = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'Sold Book: {self.book.book_name}' 
    

        
