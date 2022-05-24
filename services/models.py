from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=50)
    school_address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.school_name

class BookPurchase(models.Model):
    book_name = models.CharField(max_length=80)
    book_price = models.CharField(max_length=80, null=True, blank=True)
    purchase_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    book_stock_quantity = models.IntegerField(null=True, blank=True)
    book_image= models.ImageField(upload_to='media/books/', null=True, blank=True)

    def __str__(self):
        return self.book_name
        
