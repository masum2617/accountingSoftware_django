from django.db import models

# Create your models here.
class CompanyReceivable(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
    company_name = models.CharField(max_length=50)
    receivable_amount = models.IntegerField()
    date_of_receive = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_receive = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    # received_by = Employee
    note = models.TextField(null=True,blank=True)
    is_received = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name

class PersonalReceivable(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
    person_name = models.CharField(max_length=50)
    receivable_amount = models.IntegerField()
    date_of_receive = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_receive = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    # received_by = Employee
    note = models.TextField(null=True,blank=True)
    is_received = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.person_name

class JapanSchoolReceivable(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
    # school_name = models.ForeignKey()
    # student = models.ForeignKey()
    # student_id will be automatically comes from student table
    receivable_amount = models.IntegerField()
    date_of_receive = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_receive = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    # received_by = Employee
    note = models.TextField(null=True,blank=True)
    is_received = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)


class StudentReceivable(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Bank', 'Bank_Transfer'), 
    )
   
    # student = models.ForeignKey()
    # student_id will be automatically comes from student table
    receivable_amount = models.IntegerField()
    date_of_receive = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    method_of_receive = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='NULL')
    # received_by = Employee
    note = models.TextField(null=True,blank=True)
    is_received = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)