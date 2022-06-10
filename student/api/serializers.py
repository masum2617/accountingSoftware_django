from ..models import Student, EducationalRecord,EmergencyContact
from rest_framework import serializers


class EducationalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalRecord
        fields = '__all__'

class EmergencyContactSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = EmergencyContact
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    student_educational_record = EducationalRecordSerializer(many=True)
    emergencyContact = EmergencyContactSerializer(many=True)
    class Meta:
        model = Student
        fields = '__all__'
