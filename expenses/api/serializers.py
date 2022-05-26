from rest_framework import serializers
from expenses.models import DailyExpense

class DailyExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyExpense
        fields = '__all__'