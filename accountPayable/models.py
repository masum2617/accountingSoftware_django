from bank.models import Bank
from django.db import models

# Create your models here.

class CompanyPayable(models.Model):

    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
    company_name = models.CharField(max_length=50)
    payable_amount = models.IntegerField()
    date_of_payment = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_payment = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    # paid_by = Employee
    payment_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(null=True,blank=True)
    is_paid = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    connect_with_bank = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name

class PersonalPayable(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
    person_name = models.CharField(max_length=50, null=True)
    payable_amount = models.IntegerField()
    date_of_payment = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_payment = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    # paid_by = Employee
    payment_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(null=True,blank=True)
    is_paid = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    connect_with_bank = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class EmployeePayable(models.Model):

    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
    # employee = models.ForeignKey()
    bonus_amount = models.IntegerField(blank=True, default=0)
    loan_amount = models.IntegerField(blank=True, default=0)
    medical_expense = models.IntegerField(blank=True, default=0)
    date_of_payment = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    paid_by = models.CharField(max_length=50)
    method_of_payment = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    # paid_by = Employee
    payment_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(null=True,blank=True)
    salary_paid_status = models.BooleanField(default=False)
    loan_paid_status = models.BooleanField(default=False)
    bonus_paid_status = models.BooleanField(default=False)
    medicalExpense_paid_status = models.BooleanField(default=False)

    connect_with_bank = models.BooleanField(default=False)

class JapanSchoolPayable(models.Model):

    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
    # school = models.ForeignKey() #from services->instituition model
    other_school = models.CharField(max_length=50, null=True, blank=True)
    # student = models.ForeignKey() 
    # student_id will be automatically comes from student table
    payable_amount = models.IntegerField(blank=True, null=True)
    date_of_payment = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    paid_by = models.CharField(max_length=50)
    method_of_payment = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    payment_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(null=True,blank=True)
    is_paid = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    connect_with_bank = models.BooleanField(default=False)

class AgentPayable(models.Model):

    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
    # agent_name = models.ForeignKey()
    # school = models.ForeignKey() #from services->instituition model
    
    # student = models.ForeignKey() 
    # student_id will be automatically comes from student table
    payable_amount = models.IntegerField(blank=True, null=True)
    date_of_payment = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    paid_by = models.CharField(max_length=50)
    method_of_payment = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    payment_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(null=True,blank=True)
    is_paid = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    connect_with_bank = models.BooleanField(default=False)
