from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from .serializers import CompanyPayableSerializer

from accountPayable.models import CompanyPayable
from bank.models import Bank, Statement

class CompanyPayableListView(generics.ListCreateAPIView):
    serializer_class = CompanyPayableSerializer

    def get_queryset(self):
        return CompanyPayable.objects.all()

class CompanyPayableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyPayable.objects.all()
    serializer_class = CompanyPayableSerializer

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return CompanyPayable.objects.get(pk=pk)
        except CompanyPayable.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        companyPayable = self.get_object()
        # print("FROM PUT companyPayable: ", companyPayable.id)
        # print("REQ: ", request.data.get('payable_amount'))
        updated_expense_amount = int(request.data.get('payable_amount'))
        print("UPDATEDT AMOUNT: ", updated_expense_amount)
        try:
            companyPayable_expense = Statement.objects.get(id_of_sector=companyPayable.id)
            # grab the current expense amount from Statement
            current_expense_amount = companyPayable.payable_amount
            print("current expense amount",current_expense_amount)
            payment_bank = int(request.data.get('payment_bank'))
            print(type(payment_bank))
            # compare with coming data from request.data
            if (current_expense_amount != updated_expense_amount):
                # update amount to the bank model amount
                bank = Bank.objects.get(pk=payment_bank)
                print("GETED BANK: ", bank)
                bank.amount_of_money = (bank.amount_of_money + current_expense_amount) - updated_expense_amount
                bank.save()
                companyPayable_expense.amount_of_money = updated_expense_amount
                companyPayable_expense.save()
        except Statement.DoesNotExist:
            raise ValueError('Not Found')

        serializer = CompanyPayableSerializer(companyPayable, data=request.data)
        
        if serializer.is_valid():
            print(serializer.validated_data.get('payable_amount'))
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
