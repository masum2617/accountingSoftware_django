from accountPayable.models import CompanyPayable,AgentPayable, EmployeePayable,JapanSchoolPayable,PersonalPayable
from rest_framework import serializers

class CompanyPayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPayable
        fields = '__all__'