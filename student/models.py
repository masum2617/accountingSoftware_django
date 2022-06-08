from django.db import models
from random import randint, randrange
# Create your models here.      
def random_studentID():
    return randrange(10000, 100000,5)


class Student(models.Model):
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    student_name = models.CharField(max_length=50)
    student_id = models.IntegerField(unique=True, null=True, blank=True)
    father_name = models.CharField(max_length=50, null=True)
    mother_name = models.CharField(max_length=50,null=True)
    date_of_birth  = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    age =  models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default='NULL')
    present_address = models.TextField(null=True, blank=True)
    premanent_address = models.TextField(null=True, blank=True)
    contact_number = models.BigIntegerField()
    student_email = models.EmailField(max_length=50, unique=True)
    date_of_registration  = models.DateField(auto_now_add=True, blank=True )
    student_photo = models.ImageField(upload_to='students/', null=True, blank=True)
    

    def __str__(self):
        return self.student_name

class EmergencyContact(models.Model):
    full_name = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    contact_number = models.BigIntegerField()
    address = models.TextField(null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

class EducationalRecord(models.Model):
    education_category = models.CharField(max_length=30)
    cgpa_or_gpa = models.FloatField(null=True, blank=True)
    passing_year = models.DateField(auto_now_add=False, auto_now=False,blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.education_category


