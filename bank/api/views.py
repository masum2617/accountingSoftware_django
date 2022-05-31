from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from bank.models import Bank, Statement
from expenses.models import DailyExpense
from .serializers import BankSerializer, StatementSerializer

from expenses.models import DailyExpense

class BankListView(APIView):

    def get_queryset(self):
        # filter out by bank name
        return Bank.objects.all()

    def get(self, request):
        banks = self.get_queryset()
        # print("BANKS ", banks)
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BankListDetailView(APIView):

    def add_money(self, bank_current, expense_amount):
        return bank_current + expense_amount

    def get_object(self, pk):
        try:
            return Bank.objects.get(pk=pk)
        except Bank.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bank = self.get_object(pk)
        serializer = BankSerializer(bank)
        return Response(serializer.data)

    def put(self, request, pk):
        bank = self.get_object(pk)
        print("FROM PUT BANK: ", bank)

        serializer = BankSerializer(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        bank = self.get_object(pk)
        serializer = BankSerializer(bank, data=request.data,partial=True)
        print("SERIALIZER: ", serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bank = self.get_object(pk)
        bank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Statement Serializer
class StatementListView(generics.ListCreateAPIView):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer


class StatementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
