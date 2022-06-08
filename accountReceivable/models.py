from tkinter.tix import Tree
from django.db import models
import uuid
from student.models import Student
from employee.models import Employee,Agent
from bank.models import Bank

# Create your models here.
class CompanyReceivable(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=50)
    receivable_amount = models.IntegerField()
    date_of_receive = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_receive = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    received_by = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    received_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(null=True,blank=True)
    is_received = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    connect_with_bank = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name

class PersonalReceivable(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    person_name = models.CharField(max_length=50)
    receivable_amount = models.IntegerField()
    date_of_receive = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_receive = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    received_by = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    received_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(null=True,blank=True)
    is_received = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    connect_with_bank = models.BooleanField(default=False)

    def __str__(self):
        return self.person_name

class JapanSchoolReceivable(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    # school_name = models.ForeignKey()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    # student_id will be automatically comes from student table
    receivable_amount = models.IntegerField()
    date_of_receive = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_receive = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    received_by = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    received_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(null=True,blank=True)
    is_received = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    connect_with_bank = models.BooleanField(default=False)

    def __str__(self):
        return self.student.student_name


class StudentReceivable(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    # student_id will be automatically comes from student table
    first_installment_amount = models.IntegerField(default=0, verbose_name="First Installment")
    second_installment_amount = models.IntegerField(default=0,verbose_name="Second Installment")
    third_installment_amount = models.IntegerField(default=0,verbose_name="Third Installment")
    remaining_installment_amount = models.IntegerField(default=0,verbose_name="Remaining Amount")
    total_fees = models.IntegerField()
    date_of_receive = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_receive = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL', verbose_name="Received Through")
    received_by = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    received_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(null=True,blank=True)
    first_installment_is_receieved = models.BooleanField(default=False,verbose_name="1st Installment Paid")
    second_installment_is_receieved = models.BooleanField(default=False,verbose_name="2nd Installment Paid")
    third_installment_is_receieved = models.BooleanField(default=False,verbose_name="3rd Installment Paid")
    first_installment_is_pending = models.BooleanField(default=False)
    second_installment_is_pending = models.BooleanField(default=False)
    third_installment_is_pending = models.BooleanField(default=False)
    first_installment_is_rejected = models.BooleanField(default=False)
    second_installment_is_rejected = models.BooleanField(default=False)
    third_installment_is_rejected = models.BooleanField(default=False)
    is_full_paid = models.BooleanField(default=False)
    connect_with_bank = models.BooleanField(default=False)

    def __str__(self):
        return self.student.student_name