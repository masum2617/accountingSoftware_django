from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view

from bank.models import Bank

from expenses.models import DailyExpense
from expenses.api.serializers import DailyExpenseSerializer

@api_view(['GET', 'POST'])
def DailyExpenseList(request):
    if request.method == 'GET':
        daily_expense = DailyExpense.objects.all()
        serializer = DailyExpenseSerializer(daily_expense, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DailyExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def DailyExpenseDetail(request, pk):
    try:
        daily_expense = DailyExpense.objects.get(pk=pk)
    except DailyExpense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        print("NOT GOT IT")

    if request.method == 'GET':
        serializer = DailyExpenseSerializer(daily_expense)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DailyExpenseSerializer(daily_expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        daily_expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class DailyExpenseList(generics.ListCreateAPIView):
    
#     queryset = DailyExpense.objects.all()
#     serializer_class = DailyExpenseSerializer

# class DailyExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = DailyExpense.objects.all()
#     serializer_class = DailyExpenseSerializer
