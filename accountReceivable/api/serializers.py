from rest_framework import serializers
from ..models import CompanyReceivable,JapanSchoolReceivable,PersonalReceivable,StudentReceivable

class CompanyReceivableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CompanyReceivable
        fields = '__all__'

class PersonalReceivableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PersonalReceivable
        fields = '__all__'

class SchoolReceivableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JapanSchoolReceivable
        fields = '__all__'

class StudentReceivableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentReceivable
        fields = '__all__'