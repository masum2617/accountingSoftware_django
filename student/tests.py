from django.test import TestCase
from .models import Student
from random import randint, randrange
# Create your tests here.

def random_studentID():
    # range_start = 100**(4-1)
    # range_end = (100**4)-1
    return randrange(10000, 100000,5)

class StudentIDTest(TestCase):
    def setUp(self):
        Student.objects.create(student_name='Masum', student_id=32)
        Student.objects.create(student_name='Hasan', student_id=89)
       
    def test_studentID(self):
        """ checking for random student id """
        students = Student.objects.all()
        print("all stud: ", students)
        std = Student.objects.get(student_name='Masum')
        print("current std id= ", std.student_id)
        
        if (std.student_id != random_studentID()):
            std.student_id = random_studentID()
            # print("ALready filled with id")
        print("Updated std id: " , std.student_id)


