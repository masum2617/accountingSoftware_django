from rest_framework.response import Response
from django.contrib import messages
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from .serializers import CompanyReceivableSerializer,PersonalReceivableSerializer, SchoolReceivableSerializer,StudentReceivableSerializer
from ..helper import calculate_remaining_amount
from ..models import CompanyReceivable,StudentReceivable,JapanSchoolReceivable,PersonalReceivable
from bank.models import Bank, Statement

# remaining_amount_global = 0

# helper function

def statementOnly_for_student_receivable(student_name, payment_category,received_by,amount_of_installment,date_of_receive ,id_of_sector, bankRceived, statement_comment=""):

    bank = Bank.objects.get(pk=bankRceived)
    bank.amount_of_money = bank.amount_of_money + amount_of_installment
    bank.save()
    Statement.objects.create(coming_from_sector=student_name,payment_category=payment_category, received_by=received_by, amount_of_money=amount_of_installment, date_of_transaction=date_of_receive, bank=bank, id_of_sector=id_of_sector, comment=statement_comment)
    
        

class CompanyReceivableListView(generics.ListCreateAPIView):
    queryset = CompanyReceivable.objects.all()
    serializer_class = CompanyReceivableSerializer


class CompanyReceivableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyReceivable.objects.all()
    serializer_class = CompanyReceivableSerializer

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return CompanyReceivable.objects.get(pk=pk)
        except CompanyReceivable.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        companyReceivable = self.get_object()
        updated_receivable_amount = int(request.data.get('receivable_amount'))
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
        # get current is_Received status
        current_is_received = companyReceivable.is_received
        # get the bank from serializer.data
        received_bank = request.data.get('received_bank')
        bank = Bank.objects.get(pk=received_bank)

        try:
            # grab the current expense amount from Statement
            companyReceivable_receive_statement = Statement.objects.get(id_of_sector=companyReceivable.id)
            
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection and current_is_received==False):
                company_name = request.data.get('company_name')
                receivable_amount = int(request.data.get('receivable_amount'))
                date_of_receive = request.data.get('date_of_receive')
                received_by = request.data.get('received_by')
                bank.amount_of_money = bank.amount_of_money+receivable_amount
                bank.save()
                companyReceivable_receive_statement=Statement.objects.create(coming_from_sector=company_name,payment_category="Company Receivable", received_by=received_by, amount_of_money=receivable_amount, date_of_transaction=date_of_receive, bank=bank, id_of_sector=companyReceivable.pk)
                companyReceivable_receive_statement.save(force_insert=True)
                
            else:
                pass
        # assign company payable current amount to a variable
        current_receivable_amount = companyReceivable.receivable_amount

        if(bank_connection):
            # compare with coming data from serializer.data
            if(current_is_received==False and current_receivable_amount == updated_receivable_amount):
                
                bank.amount_of_money = (bank.amount_of_money + current_receivable_amount) 
                bank.save()
                companyReceivable_receive_statement.amount_of_money = current_receivable_amount
                companyReceivable_receive_statement.save()

            elif (current_is_received==True and current_receivable_amount != updated_receivable_amount):
                # update amount to the bank model amount
                bank.amount_of_money = (bank.amount_of_money - current_receivable_amount) + updated_receivable_amount
                bank.save()
                companyReceivable_receive_statement.amount_of_money = updated_receivable_amount
                companyReceivable_receive_statement.save()
            else:
                messages.warning(serializer, 'Nothing to update!')
        elif(bank_connection == False):
            # if bank connection is changed to false (from true)
            bank.amount_of_money = bank.amount_of_money - current_receivable_amount 
            bank.save()
            # companyPayable_expense_statement.amount_of_money = updated_expense_amount
            companyReceivable_receive_statement.delete()
            messages.success(serializer, "deleted statement")

        serializer = CompanyReceivableSerializer(companyReceivable, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CompanyPayable END


# PERSONAL Payable START

class PersonalReceivableListView(generics.ListCreateAPIView):
    queryset = PersonalReceivable.objects.all()
    serializer_class = PersonalReceivableSerializer

class PersonalReceivableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalReceivable.objects.all()
    serializer_class = PersonalReceivableSerializer

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return PersonalReceivable.objects.get(pk=pk)
        except PersonalReceivable.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        personalReceivable = self.get_object()
        updated_receivable_amount = int(request.data.get('receivable_amount'))
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
        # get current is_received status
        current_is_received = personalReceivable.is_received
        # get the bank from serializer.data
        received_bank = request.data.get('received_bank')
        bank = Bank.objects.get(pk=received_bank)

        try:
            # grab the current expense amount from Statement
            personalReceivable_receive_statement = Statement.objects.get(id_of_sector=personalReceivable.id)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection and current_is_received == False):
                person_name = request.data.get('person_name')
                receivable_amount = int(request.data.get('receivable_amount'))
                date_of_receive = request.data.get('date_of_receive')
                received_by = request.data.get('received_by')
                bank.amount_of_money = bank.amount_of_money + receivable_amount
                bank.save()
                personalReceivable_receive_statement=Statement.objects.create(coming_from_sector=person_name,payment_category="Personal Receivable", received_by=received_by, amount_of_money=receivable_amount, date_of_transaction=date_of_receive, bank=bank, id_of_sector=personalReceivable.pk)
                personalReceivable_receive_statement.save(force_insert=True)
                
            else:
                messages.warning(request, "Something wrong check again!")
        # assign company payable current amount to a variable
        current_receivable_amount = personalReceivable.receivable_amount

        if(bank_connection):
            # compare with coming data from serializer.data
            if(current_is_received == False and current_receivable_amount == updated_receivable_amount):
                bank.amount_of_money = (bank.amount_of_money + current_receivable_amount) - updated_receivable_amount
                bank.save()
                personalReceivable_receive_statement.amount_of_money = current_receivable_amount
                personalReceivable_receive_statement.save()

            elif (current_is_received == True and current_receivable_amount != updated_receivable_amount):
                # update amount to the bank model amount
                # bank = Bank.objects.get(pk=received_bank)
                bank.amount_of_money = (bank.amount_of_money - current_receivable_amount) + updated_receivable_amount
                bank.save()
                personalReceivable_receive_statement.amount_of_money = updated_receivable_amount
                personalReceivable_receive_statement.save()
            else:
                messages.warning(request, 'Nothing to update!')
        elif(bank_connection == False):
            # if bank connection is changed to false (from true
            bank.amount_of_money = bank.amount_of_money - current_receivable_amount 
            bank.save()
            personalReceivable_receive_statement.delete()
            messages.success(request, "deleted statement")

        serializer = PersonalReceivableSerializer(personalReceivable, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PERSONAL Payable END


# JAPAN SCHOOL START
class SchoolReceivableListView(generics.ListCreateAPIView):
    queryset = JapanSchoolReceivable.objects.all()
    serializer_class = SchoolReceivableSerializer


class SchoolReceivableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JapanSchoolReceivable.objects.all()
    serializer_class = SchoolReceivableSerializer

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return JapanSchoolReceivable.objects.get(pk=pk)
        except JapanSchoolReceivable.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        schoolReceivable = self.get_object()
        updated_receivable_amount = int(request.data.get('receivable_amount'))
        # get the current is_received status
        current_is_received = schoolReceivable.is_received
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
        # get the bank 
        received_bank = request.data.get('received_bank')
        bank = Bank.objects.get(pk=received_bank)

        try:
            # grab the current expense amount from Statement
            schoolReceivable_receive_statement = Statement.objects.get(id_of_sector=schoolReceivable.id)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection and current_is_received == False):
                school_name = request.data.get('school_name')
                receivable_amount = int(request.data.get('receivable_amount'))
                date_of_receive = request.data.get('date_of_receive')
                received_by = request.data.get('received_by')
                bank.amount_of_money = bank.amount_of_money + receivable_amount
                bank.save()
                schoolReceivable_receive_statement = Statement.objects.create(coming_from_sector=school_name.school_name,payment_category="School Receivable", received_by=received_by, amount_of_money=receivable_amount, date_of_transaction=date_of_receive, bank=bank, id_of_sector=schoolReceivable.pk)
                schoolReceivable_receive_statement.save(force_insert=True)
                
            else:
                pass
        # assign company payable current amount to a variable
        current_receivable_amount = schoolReceivable.receivable_amount

        if(bank_connection):
            # compare with coming data from serializer.data
            if(current_is_received == False and current_receivable_amount == updated_receivable_amount):
                bank.amount_of_money = (bank.amount_of_money + current_receivable_amount)
                bank.save()
                schoolReceivable_receive_statement.amount_of_money = current_receivable_amount
                schoolReceivable_receive_statement.save()

            elif (current_is_received == True and current_receivable_amount != updated_receivable_amount):
                # update amount to the bank model amount
                bank.amount_of_money = (bank.amount_of_money - current_receivable_amount) + updated_receivable_amount
                bank.save()
                schoolReceivable_receive_statement.amount_of_money = updated_receivable_amount
                schoolReceivable_receive_statement.save()
            else:
                messages.warning(serializer, 'Nothing to update!')
        elif(bank_connection == False):
            # if bank connection is changed to false (from true
            bank.amount_of_money = bank.amount_of_money - current_receivable_amount 
            bank.save()
            schoolReceivable_receive_statement.delete()
            messages.success(serializer, "deleted statement")

        serializer = SchoolReceivableSerializer(schoolReceivable, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# JAPAN SCHOOL Payable END

# Student Receivable START
class StudentlReceivableListView(generics.ListCreateAPIView):
    queryset = StudentReceivable.objects.all()
    serializer_class = StudentReceivableSerializer

class StudentReceivableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentReceivable.objects.all()
    serializer_class = StudentReceivableSerializer

    # helper function

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return StudentReceivable.objects.get(pk=pk)
        except StudentReceivable.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        studentReceivable = self.get_object()
        
        remaining_amount_global = studentReceivable.remaining_installment_amount
        updated_first_installment_amount = int(request.data.get('first_installment_amount'))
        updated_second_installment_amount = int(request.data.get('second_installment_amount'))
        updated_third_installment_amount = int(request.data.get('third_installment_amount'))
        total_fees = int(request.data.get('total_fees'))
        
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
        # get the bank from serializer.data
        received_bank = request.data.get('received_bank')
       
        
            # create Statement for particular expense if bank
        if(bank_connection):
            student_name = request.data.get('student')
            date_of_receive = request.data.get('date_of_receive')
            received_by = request.data.get('received_by')
            first_installment_is_receieved = request.data.get('first_installment_is_receieved')
            second_installment_is_receieved = request.data.get('second_installment_is_receieved')
            third_installment_is_receieved = request.data.get('third_installment_is_receieved')
            
            # check if the installment are paid
            if (updated_first_installment_amount > 0 and first_installment_is_receieved==True and updated_second_installment_amount == 0 and updated_third_installment_amount == 0):
                
                statementOnly_for_student_receivable(student_name, "Student Receivable", received_by, updated_first_installment_amount, date_of_receive, studentReceivable.pk, received_bank)
                # update remaining amount
                remaining_amount_global = calculate_remaining_amount(total_fees, updated_first_installment_amount, updated_second_installment_amount, updated_third_installment_amount)

            elif (updated_first_installment_amount > 0 and second_installment_is_receieved and updated_second_installment_amount > 0 and updated_third_installment_amount == 0):
                statementOnly_for_student_receivable(student_name, "Student Receivable", received_by, updated_second_installment_amount, date_of_receive, studentReceivable.pk, received_bank)
                # update remaining amount
                remaining_amount_global = calculate_remaining_amount(total_fees, updated_first_installment_amount, updated_second_installment_amount, updated_third_installment_amount)

            elif (updated_first_installment_amount > 0 and third_installment_is_receieved and updated_second_installment_amount > 0 and updated_third_installment_amount > 0):
                statementOnly_for_student_receivable(student_name, "Student Receivable", received_by, updated_third_installment_amount, date_of_receive, studentReceivable.pk, received_bank)
                # update remaining amount to the global variable 

                remaining_amount_global = calculate_remaining_amount(total_fees, updated_first_installment_amount, updated_second_installment_amount, updated_third_installment_amount)  
        else:
            pass

        serializer = StudentReceivableSerializer(studentReceivable, data=request.data)
        
        if serializer.is_valid():
            # save the remaining amount through serializer
            serializer.validated_data['remaining_installment_amount']=str(remaining_amount_global)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
