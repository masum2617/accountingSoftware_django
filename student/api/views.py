from rest_framework import generics
from .serializers import EmergencyContactSerializer,EducationalRecordSerializer,StudentSerializer
from student.models import Student,EducationalRecord,EmergencyContact

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EducationalRecordListView(generics.ListCreateAPIView):
    queryset = EducationalRecord.objects.all()
    serializer_class = EducationalRecordSerializer
    
class EducationalRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EducationalRecord.objects.all()
    serializer_class = EducationalRecordSerializer

class EmergencyContactRecordListView(generics.ListCreateAPIView):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer
    
class EmergencyContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer