from django.db import models
from bank.models import Bank

# Create your models here.
class DailyExpense(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank Transfer'), 
    )
    expense_type  = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity= models.IntegerField()
    date_of_payment = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_payment = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    note = models.TextField(null=True,blank=True)
    payment_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    # paid_by = models.ForeignKey() #employee

    def __str__(self):
        return self.expense_type

class OfficeRentExpense(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank Transfer'), 
    )
    expense_type = models.CharField(max_length=50, default='Office Rent')
    monthly_cost = models.IntegerField()
    date_of_payment = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_payment = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    note = models.TextField(null=True,blank=True)
    payment_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    # paid_by = models.ForeignKey() #employee

    def __str__(self):
        return self.expense_type

class UtilityExpense(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank Transfer'), 
    )
    MONTH = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),


    )
    utility_category  = models.CharField(max_length=50)
    monthly_bill = models.IntegerField()
    bill_month = models.CharField(max_length=20, choices=MONTH, default='NULL', blank=True)
    date_of_payment = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_payment = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    note = models.TextField(null=True,blank=True)
    payment_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    # paid_by = models.ForeignKey() #employee

    def __str__(self):
        return self.utility_category

class DocumentRenewalExpense(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank Transfer'), 
    )
    document_name  = models.CharField(max_length=50)
    issue_authority  = models.CharField(max_length=50, null=True, blank=True)
    renewal_amount = models.IntegerField()
    renewal_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_payment = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    note = models.TextField(null=True,blank=True)
    payment_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    # paid_by = models.ForeignKey() #employee
    
    def __str__(self):
        return self.document_name

class MiscExpense(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank Transfer'), 
    )
    expense_name  = models.CharField(max_length=50)
    price = models.IntegerField()
    date_of_payment = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_payment = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    note = models.TextField(null=True,blank=True)
    payment_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    # paid_by = models.ForeignKey() #employee

    def __str__(self):
        return self.expense_name

    
