from django.db import models

# Create your models here.
class Bank(models.Model):
    bank_name = models.CharField(max_length=50)
    bank_branch = models.CharField(max_length=50, null=True)
    account_num = models.BigIntegerField()
    amount_of_money = models.BigIntegerField()

    class Meta:
        ordering = ['id'] #order data by id ascending order in the admin panel

    def __str__(self):
        return self.bank_name

class Statement(models.Model):
    coming_from_sector = models.CharField(max_length=50, null=True, blank=True)
    payment_category = models.CharField(max_length=50, null=True, blank=True)
    paid_to = models.CharField(max_length=80, null=True, blank=True)
    paid_to_id = models.IntegerField(null=True,blank=True)
    received_by = models.CharField(max_length=100, null=True, blank=True)
    received_by_id = models.IntegerField(null=True,blank=True)
    amount_of_money = models.IntegerField(null=True,blank=True)
    date_of_transaction = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    id_of_sector = models.CharField(max_length=128, null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'Coming From: {self.coming_from_sector}'