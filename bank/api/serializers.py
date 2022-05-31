from bank.models import Bank, Statement
from rest_framework import serializers

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = '__all__'