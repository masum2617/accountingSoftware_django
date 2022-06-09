from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib import messages
from .serializers import AssetSerializer
from inventory.models import Asset
from bank.models import Bank,Statement

class AssetListView(generics.ListCreateAPIView):
    serializer_class = AssetSerializer

    def get_queryset(self):
        return Asset.objects.all()

class AssetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Asset.objects.get(pk=pk)
        except Asset.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        asset = self.get_object()
        # assign current asset price to a variable
        current_asset_price = asset.asset_price
        # get the current is_paid status
        current_is_paid= asset.is_paid
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')

        payment_bank = request.data.get('payment_bank')
        bank = Bank.objects.get(pk=payment_bank)

        try:
            # grab the current expense amount from Statement
            asset_expense_statement = Statement.objects.get(id_of_sector=asset.id)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection):
                asset_name = request.data.get('asset_name')
                updated_asset_price = int(request.data.get('asset_price'))
                purchase_date = request.data.get('purchase_date')
                asset_expense_statement=Statement.objects.create(coming_from_sector=asset_name,payment_category="Asset Payment", amount_of_money=updated_asset_price, date_of_transaction=purchase_date, bank=bank, id_of_sector=asset.id)
                asset_expense_statement.save()
            else:
                pass

        # getting the linked bank from requested data for updating
        payment_bank = int(request.data.get('payment_bank'))

        if(bank_connection): #if true bank connection
            # compare with coming data from request.data
            
            if(current_is_paid == False and current_asset_price == updated_asset_price):
                bank.amount_of_money = bank.amount_of_money + current_asset_price
                bank.save()
            elif(current_is_paid == True and current_asset_price != updated_asset_price):
                bank.amount_of_money = (bank.amount_of_money - current_asset_price) + updated_asset_price
                bank.save()

            # update statement
            asset_expense_statement.amount_of_money = updated_asset_price
            asset_expense_statement.save()
            # else:
            messages.success(request, "Successfully UPDATED")
        else:
            bank.amount_of_money = bank.amount_of_money - current_asset_price
            bank.save()
            asset_expense_statement.delete()
            messages.success(request, "deleted statement")

        serializer = AssetSerializer(asset, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)