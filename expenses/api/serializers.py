from rest_framework import serializers
from expenses.models import DailyExpense,DocumentRenewalExpense,MiscExpense,OfficeRentExpense,UtilityExpense

class DailyExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyExpense
        fields = '__all__'

class DocumentRenewalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentRenewalExpense
        fields = '__all__'

class MiscExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiscExpense
        fields = '__all__'

class OfficeRentExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeRentExpense
        fields = '__all__'

class UtilityxpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilityExpense
        fields = '__all__'