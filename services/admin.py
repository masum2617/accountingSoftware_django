from django.contrib import admin
from .models import School, Book,BookSale
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','book_name','book_price','book_stock_quantity', 'purchase_date' ]

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id','school_name' ]

class BookSaleAdmin(admin.ModelAdmin):
    list_display = ['book','price_of_each','sold_quantity', 'total_price','sold_to_student','sold_to_other' ]

admin.site.register(School,SchoolAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(BookSale,BookSaleAdmin)
