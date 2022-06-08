from statistics import mode
from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name =  models.CharField(max_length=50)
    employee_role =  models.CharField(max_length=80)
    employee_email =  models.EmailField(max_length=50, unique=True,null=True)
    employee_salary =  models.IntegerField()
    employee_address =  models.CharField(max_length=100, blank=True)
    employee_phone =  models.BigIntegerField()
    employee_date_joined  = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    employee_photo = models.ImageField(upload_to='employees/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.employee_name

class Agent(models.Model):
    agent_name =  models.CharField(max_length=50)
    agent_email =  models.EmailField(max_length=50, unique=True, null=True)
    agent_address =  models.CharField(max_length=100, null=True, blank=True)
    agent_phone = models.BigIntegerField()
    agent_date_joined  = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    agent_photo = models.ImageField(upload_to='agents/', null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.agent_name)
