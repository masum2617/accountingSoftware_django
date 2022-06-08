from traceback import print_tb
from django.test import TestCase
from .models import Student
from random import randint, randrange
# Create your tests here.

import uuid 

# def random_studentID():
#     # range_start = 100**(4-1)
#     # range_end = (100**4)-1
#     return randrange(10000, 100000,5)
def random_studentID():
    student_id = str(uuid.uuid4().int)
    return student_id[:6]


class StudentIDTest(TestCase):

    def test_studentID(self):
        print(random_studentID())

        # std = Student.objects.get(student_name='Masum')
        # print("current std id= ", std.student_id)
        
        # if (std.student_id != random_studentID()):
        #     std.student_id = random_studentID()
        #     # print("ALready filled with id")
        # print("Updated std id: " , std.student_id)


