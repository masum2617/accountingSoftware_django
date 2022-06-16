from inventory.models import Asset
from rest_framework import serializers

class AssetSerializer(serializers.ModelSerializer):
    # StringRelatedField may be used to represent the target of the relationship using its __str__ method.(Here for bank foreign key relations)
    # payment_bank = serializers.StringRelatedField()
    class Meta:
        model = Asset
        fields = '__all__'
