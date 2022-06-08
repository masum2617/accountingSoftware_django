from django.db import models
from bank.models import Bank
from employee.models import Employee
import uuid

# Create your models here.
class Asset(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank Transfer'), 
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    asset_name  = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    asset_price = models.IntegerField()
    purchase_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    depreciation_percent = models.IntegerField(null=True, blank=True)
    method_of_payment = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL', blank=True)
    note = models.TextField(null=True,blank=True)
    payment_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    is_paid = models.BooleanField(default=False) 
    paid_by = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    connect_with_bank = models.BooleanField(default=False)

    def __str__(self):
        return self.asset_name

