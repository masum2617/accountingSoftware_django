from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db.models import F

from .models import BookSale,Book

@receiver(pre_save, sender=BookSale)
def bookSale_pre_save(sender,instance,*args, **kwargs):
    if instance.total_price is None:
        instance.total_price = str(int(instance.sold_quantity) * int(instance.price_of_each))

    # reduce quantity of the book model
    book = Book.objects.get(book_name=instance.book.book_name)
    book.book_stock_quantity = F('book_stock_quantity') - int(instance.sold_quantity)
    book.save()
        