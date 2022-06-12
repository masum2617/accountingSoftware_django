from rest_framework import generics
from rest_framework.response import Response
from django.contrib import messages
from rest_framework import status
from django.http import Http404


from bank.models import Bank,Statement
from expenses.models import DailyExpense,UtilityExpense,DocumentRenewalExpense,MiscExpense
from expenses.api.serializers import DailyExpenseSerializer,DocumentRenewalSerializer,MiscExpenseSerializer,OfficeRentExpenseSerializer,UtilityxpenseSerializer
from expenses.models import OfficeRentExpense

class DailyExpenseList(generics.ListCreateAPIView):
    
    queryset = DailyExpense.objects.all()
    serializer_class = DailyExpenseSerializer

class DailyExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyExpense.objects.all()
    serializer_class = DailyExpenseSerializer
    
    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return DailyExpense.objects.get(pk=pk)
        except DailyExpense.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        dailyExpense = self.get_object()
        updated_expense_amount = int(request.data.get('price'))
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
         # get the current is_paid status from obj
        current_is_paid = dailyExpense.is_paid
        # assign company payable current amount to a variable
        current_expense_amount = dailyExpense.price

        payment_bank = request.data.get('payment_bank')
        bank = Bank.objects.get(pk=payment_bank)

        try:
            # grab the current expense amount from Statement
            daily_expense_statement = Statement.objects.get(id_of_sector=dailyExpense.id)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection):
                expense_type = request.data.get('expense_type')
                payable_amount = request.data.get('price')
                date_of_transaction = request.data.get('date_of_payment')
                daily_expense_statement=Statement.objects.create(coming_from_sector=expense_type, payment_category="Daily Expense",amount_of_money=payable_amount, date_of_transaction=date_of_transaction, bank=bank, id_of_sector=dailyExpense.id)
                daily_expense_statement.save()
            else:
                pass
        # getting the linked bank from requested data for updating
        if(bank_connection and payment_bank is not None):
            # compare with coming data from request.data
            if (current_is_paid == False and current_expense_amount == updated_expense_amount):
                # update amount to the bank model amount
                bank.amount_of_money = bank.amount_of_money - current_expense_amount 
                bank.save()
            # statement created before now want to update it
            elif (current_is_paid == True and current_expense_amount != updated_expense_amount):
                # update amount to the bank model amount
                bank.amount_of_money = (bank.amount_of_money + current_expense_amount) - updated_expense_amount
                bank.save()
            else:
                messages.warning(request, 'Please Check again!')
            daily_expense_statement.amount_of_money = updated_expense_amount
            daily_expense_statement.save()
        elif(bank_connection == False):
            bank.amount_of_money = bank.amount_of_money + current_expense_amount
            bank.save()
            daily_expense_statement.delete()
            messages.success(request, "deleted daily expense statement")

        serializer = DailyExpenseSerializer(dailyExpense, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UtilityExpenseList(generics.ListCreateAPIView):
    
    queryset = UtilityExpense.objects.all()
    serializer_class = UtilityxpenseSerializer

class UtilityExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UtilityExpense.objects.all()
    serializer_class = UtilityxpenseSerializer
    
    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return UtilityExpense.objects.get(pk=pk)
        except UtilityExpense.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        utilityExpense = self.get_object()
        updated_expense_amount = int(request.data.get('monthly_bill'))
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
         # get the current is_paid status from obj
        current_is_paid = utilityExpense.is_paid
        # assign company payable current amount to a variable
        current_expense_amount = utilityExpense.monthly_bill

        payment_bank = request.data.get('payment_bank')
        bank = Bank.objects.get(pk=payment_bank)

        try:
            # grab the current expense amount from Statement
            utility_expense_statement = Statement.objects.get(id_of_sector=utilityExpense.id)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection):
                expense_type = request.data.get('expense_type')
                payable_amount = request.data.get('monthly_bill')
                date_of_transaction = request.data.get('date_of_payment')
                utility_expense_statement=Statement.objects.create(coming_from_sector=expense_type, payment_category="Utility Expense",amount_of_money=payable_amount, date_of_transaction=date_of_transaction, bank=bank, id_of_sector=utilityExpense.id)
                utility_expense_statement.save()
            else:
                pass
        # getting the linked bank from requested data for updating
        if(bank_connection and payment_bank is not None):
            # compare with coming data from request.data
            if (current_is_paid == False and current_expense_amount == updated_expense_amount):
                # update amount to the bank model amount
                bank.amount_of_money = bank.amount_of_money - current_expense_amount 
                bank.save()
            # statement created before now want to update it
            elif (current_is_paid == True and current_expense_amount != updated_expense_amount):
                # update amount to the bank model amount
                bank.amount_of_money = (bank.amount_of_money + current_expense_amount) - updated_expense_amount
                bank.save()
            else:
                messages.warning(request, 'Please Check again!')
            utility_expense_statement.amount_of_money = updated_expense_amount
            utility_expense_statement.save()
        elif(bank_connection == False):
            bank.amount_of_money = bank.amount_of_money + current_expense_amount
            bank.save()
            utility_expense_statement.delete()
            messages.success(request, "deleted utility expense statement")

        serializer = UtilityxpenseSerializer(utilityExpense, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# office rental cost
class OfficeRentExpenseList(generics.ListCreateAPIView):
    
    queryset = OfficeRentExpense.objects.all()
    serializer_class = OfficeRentExpenseSerializer

class OfficeRentExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfficeRentExpense.objects.all()
    serializer_class = OfficeRentExpenseSerializer
    
    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return OfficeRentExpense.objects.get(pk=pk)
        except OfficeRentExpense.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        office_rent = self.get_object()
        updated_expense_amount = int(request.data.get('monthly_rent_cost'))
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
         # get the current is_paid status from obj
        current_is_paid = office_rent.is_paid
        # assign company payable current amount to a variable
        current_expense_amount = office_rent.monthly_rent_cost

        payment_bank = request.data.get('payment_bank')
        bank = Bank.objects.get(pk=payment_bank)

        try:
            # grab the current expense amount from Statement
            officeRent_expense_statement = Statement.objects.get(id_of_sector=office_rent.id)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection):
                expense_type = request.data.get('expense_type')
                payable_amount = request.data.get('monthly_rent_cost')
                date_of_transaction = request.data.get('date_of_payment')
                officeRent_expense_statement = Statement.objects.create(coming_from_sector=expense_type, payment_category="Office Rent Expense",amount_of_money=payable_amount, date_of_transaction=date_of_transaction, bank=bank, id_of_sector=office_rent.id)
                officeRent_expense_statement.save()
            else:
                pass
        # getting the linked bank from requested data for updating
        if(bank_connection and payment_bank is not None):
            # compare with coming data from request.data
            if (current_is_paid == False and current_expense_amount == updated_expense_amount):
                # update amount to the bank model amount
                bank.amount_of_money = bank.amount_of_money - current_expense_amount 
                bank.save()
            # statement created before now want to update it
            elif (current_is_paid == True and current_expense_amount != updated_expense_amount):
                # update amount to the bank model amount
                bank.amount_of_money = (bank.amount_of_money + current_expense_amount) - updated_expense_amount
                bank.save()
            else:
                messages.warning(request, 'Please Check again!')
            officeRent_expense_statement.amount_of_money = updated_expense_amount
            officeRent_expense_statement.save()
        elif(bank_connection == False):
            bank.amount_of_money = bank.amount_of_money + current_expense_amount
            bank.save()
            officeRent_expense_statement.delete()
            messages.success(request, "deleted office rent statement")

        serializer = OfficeRentExpenseSerializer(office_rent, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# document renewawl expense
class DocumentRenewalExpenseList(generics.ListCreateAPIView):
    
    queryset = DocumentRenewalExpense.objects.all()
    serializer_class = DocumentRenewalSerializer

class DocumentRenewalExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocumentRenewalExpense.objects.all()
    serializer_class = DocumentRenewalSerializer
    
    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return DocumentRenewalExpense.objects.get(pk=pk)
        except DocumentRenewalExpense.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        document_renewal = self.get_object()
        updated_expense_amount = int(request.data.get('renewal_amount'))
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
         # get the current is_paid status from obj
        current_is_paid = document_renewal.is_paid
        # assign company payable current amount to a variable
        current_expense_amount = document_renewal.renewal_amount

        payment_bank = request.data.get('payment_bank')
        bank = Bank.objects.get(pk=payment_bank)

        try:
            # grab the current expense amount from Statement
            officeRent_expense_statement = Statement.objects.get(id_of_sector=document_renewal.id)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection):
                expense_type = request.data.get('expense_type')
                payable_amount = request.data.get('renewal_amount')
                date_of_transaction = request.data.get('date_of_payment')
                documentRenewal_expense_statement = Statement.objects.create(coming_from_sector=expense_type, payment_category="Document Renewal Expense",amount_of_money=payable_amount, date_of_transaction=date_of_transaction, bank=bank, id_of_sector=document_renewal.id)
                documentRenewal_expense_statement.save()
            else:
                pass
        # getting the linked bank from requested data for updating
        if(bank_connection and payment_bank is not None):
            # compare with coming data from request.data
            if (current_is_paid == False and current_expense_amount == updated_expense_amount):
                # update amount to the bank model amount
                bank.amount_of_money = bank.amount_of_money - current_expense_amount 
                bank.save()
            # statement created before now want to update it
            elif (current_is_paid == True and current_expense_amount != updated_expense_amount):
                # update amount to the bank model amount
                bank.amount_of_money = (bank.amount_of_money + current_expense_amount) - updated_expense_amount
                bank.save()
            else:
                messages.warning(request, 'Please Check again!')
            # update statement
            documentRenewal_expense_statement.amount_of_money = updated_expense_amount
            documentRenewal_expense_statement.save()
        
        elif(bank_connection == False):
            bank.amount_of_money = bank.amount_of_money + current_expense_amount
            bank.save()
            documentRenewal_expense_statement.delete()
            messages.success(request, "deleted office rent statement")

        serializer = DocumentRenewalSerializer(document_renewal, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Miscellaneous Expense
class MiscExpenseList(generics.ListCreateAPIView):
    queryset = MiscExpense.objects.all()
    serializer_class = MiscExpenseSerializer

class MiscExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MiscExpense.objects.all()
    serializer_class = MiscExpenseSerializer
    
    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return MiscExpense.objects.get(pk=pk)
        except MiscExpense.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        misc_expense = self.get_object()
        updated_expense_amount = int(request.data.get('price'))
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
         # get the current is_paid status from obj
        current_is_paid = misc_expense.is_paid
        # assign company payable current amount to a variable
        current_expense_amount = misc_expense.renewal_amount

        payment_bank = request.data.get('payment_bank')
        bank = Bank.objects.get(pk=payment_bank)

        try:
            # grab the current expense amount from Statement
            misc_expense_statement = Statement.objects.get(id_of_sector=misc_expense.id)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection):
                expense_type = request.data.get('expense_type')
                payable_amount = request.data.get('price')
                date_of_transaction = request.data.get('date_of_payment')
                misc_expense_statement = Statement.objects.create(coming_from_sector=expense_type, payment_category="Miscellaneous Expense",amount_of_money=payable_amount, date_of_transaction=date_of_transaction, bank=bank, id_of_sector=misc_expense.id)
                misc_expense_statement.save()
            else:
                pass
        # getting the linked bank from requested data for updating
        if(bank_connection and payment_bank is not None):
            # compare with coming data from request.data
            if (current_is_paid == False and current_expense_amount == updated_expense_amount):
                # update amount to the bank model amount
                bank.amount_of_money = bank.amount_of_money - current_expense_amount 
                bank.save()
            # statement created before now want to update it
            elif (current_is_paid == True and current_expense_amount != updated_expense_amount):
                # update amount to the bank model amount
                bank.amount_of_money = (bank.amount_of_money + current_expense_amount) - updated_expense_amount
                bank.save()
            else:
                messages.warning(request, 'Please Check again!')
            # update statement
            misc_expense_statement.amount_of_money = updated_expense_amount
            misc_expense_statement.save()
        
        elif(bank_connection == False):
            bank.amount_of_money = bank.amount_of_money + current_expense_amount
            bank.save()
            misc_expense_statement.delete()
            messages.success(request, "deleted office rent statement")

        serializer = MiscExpenseSerializer(misc_expense, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
