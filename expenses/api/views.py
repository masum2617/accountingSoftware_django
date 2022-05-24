from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from expenses.models import DailyExpense
from expenses.api.serializers import DailyExpenseSerializer

class DailyExpenseList(APIView):
    def get(self, request):
        daily_expense = DailyExpense.objects.all()
        serializer = DailyExpenseSerializer(daily_expense, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DailyExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

