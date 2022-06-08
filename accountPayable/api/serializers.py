from accountPayable.models import CompanyPayable,AgentPayable, EmployeePayable,JapanSchoolPayable,PersonalPayable
from rest_framework import serializers

class CompanyPayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPayable
        fields = '__all__'

class PersonalPayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalPayable
        fields = '__all__'

class SchoolPayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = JapanSchoolPayable
        fields = '__all__'

class AgentPayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentPayable
        fields = '__all__'

class EmployeePayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePayable
        fields = '__all__'