from rest_framework.response import Response
from django.contrib import messages
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from .serializers import CompanyPayableSerializer,PersonalPayableSerializer, SchoolPayableSerializer,AgentPayableSerializer,EmployeePayableSerializer

from accountPayable.models import CompanyPayable, PersonalPayable, AgentPayable,EmployeePayable,JapanSchoolPayable
from bank.models import Bank, Statement

# Company Payable
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
        updated_expense_amount = int(request.data.get('payable_amount'))
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
        # get the bank obj
        payment_bank = request.data.get('payment_bank')
        bank = Bank.objects.get(pk=payment_bank)
         # assign company payable current amount to a variable
        current_expense_amount = companyPayable.payable_amount
        # get the current is_paid status from obj
        current_is_paid = companyPayable.is_paid

        try:
            # grab the current expense amount from Statement
            companyPayable_expense_statement = Statement.objects.get(id_of_sector=companyPayable.id)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection):
                company_name = request.data.get('company_name')
                payable_amount = request.data.get('payable_amount')
                date_of_transaction = request.data.get('date_of_payment')
                companyPayable_expense_statement=Statement.objects.create(coming_from_sector=company_name,category="Company Payable", amount_of_money=payable_amount, date_of_transaction=date_of_transaction, bank=bank, id_of_sector=companyPayable.id)
                companyPayable_expense_statement.save()
            else:
                pass
       
        if(bank_connection and payment_bank is not None):
            # compare with coming data from request.data
            # if the statement created just now
            if (current_is_paid == False and current_expense_amount == updated_expense_amount ):
                bank.amount_of_money = (bank.amount_of_money - current_expense_amount)
                bank.save()
            # statement created before now want to update it
            elif (current_is_paid == True and current_expense_amount != updated_expense_amount):
                # update amount to the bank model amount
                bank.amount_of_money = (bank.amount_of_money + current_expense_amount) - updated_expense_amount
                bank.save()
                companyPayable_expense_statement.amount_of_money = updated_expense_amount
                companyPayable_expense_statement.save()
            else:
                messages.warning(request, 'Nothing to update!')
        
        elif (not bank_connection):
            bank.amount_of_money = bank.amount_of_money + current_expense_amount
            bank.save()
            companyPayable_expense_statement.delete()
            messages.success(request, "deleted statement for company Payable")

        serializer = CompanyPayableSerializer(companyPayable, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PersonalPayable 
class PersonalPayableListView(generics.ListCreateAPIView):
    serializer_class = PersonalPayableSerializer

    def get_queryset(self):
        return PersonalPayable.objects.all()

class PersonalPayableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalPayable.objects.all()
    serializer_class = PersonalPayableSerializer

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return PersonalPayable.objects.get(pk=pk)
        except PersonalPayable.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        personalPayable = self.get_object()
        # assign company payable current amount to a variable
        current_expense_amount = personalPayable.payable_amount
        updated_expense_amount = int(request.data.get('payable_amount'))
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
        # get the current is_paid status from obj
        current_is_paid = personalPayable.is_paid
        # get the connected bank
        payment_bank = request.data.get('payment_bank')
        bank = Bank.objects.get(pk=payment_bank)

        try:
            # grab the current expense amount from Statement
            personalPayable_expense_statement = Statement.objects.get(id_of_sector=personalPayable.pk)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection):
                person_name = request.data.get('person_name')
                payable_amount = request.data.get('payable_amount')
                date_of_transaction = request.data.get('date_of_payment')
                personalPayable_expense_statement=Statement.objects.create(coming_from_sector=person_name,payment_category="Personal Payable", amount_of_money=payable_amount, date_of_transaction=date_of_transaction, bank=bank, id_of_sector=personalPayable.id)
                personalPayable_expense_statement.save()
            else:
                pass

        if(bank_connection and payment_bank is not None):
            # compare with coming data from request.data
            # if the statement created just now
            if (current_is_paid == False and current_expense_amount == updated_expense_amount):
                # update amount to the bank model amount
                bank.amount_of_money = bank.amount_of_money - current_expense_amount 
                bank.save()

            # statement created before now want to update it
            elif (current_is_paid == True and current_expense_amount != updated_expense_amount):
                # update amount to the bank model amount
                print("FROM UPDATING NOT MATch")
                bank.amount_of_money = (bank.amount_of_money + current_expense_amount) - updated_expense_amount
                bank.save()
                personalPayable_expense_statement.amount_of_money = updated_expense_amount
                personalPayable_expense_statement.save()
            else:
                messages.warning(request, 'Something Wrong! Please Check again!')
        if (not bank_connection):
            bank.amount_of_money = bank.amount_of_money + current_expense_amount
            bank.save()
            personalPayable_expense_statement.delete()
            messages.success(request, "deleted  Personal Payabale statement")

        serializer = PersonalPayableSerializer(personalPayable, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# End of Personal Payable

# Japan School Payable Start
class SchoolPayableListView(generics.ListCreateAPIView):
    serializer_class = SchoolPayableSerializer

    def get_queryset(self):
        return JapanSchoolPayable.objects.all()

class SchoolPayableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JapanSchoolPayable.objects.all()
    serializer_class = SchoolPayableSerializer

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return JapanSchoolPayable.objects.get(pk=pk)
        except JapanSchoolPayable.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        schoolPayable = self.get_object()
        updated_expense_amount = int(request.data.get('payable_amount'))
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
        # get the bank obj
        payment_bank = request.data.get('payment_bank')
        bank = Bank.objects.get(pk=payment_bank)
        # assign company payable current amount to a variable
        current_expense_amount = schoolPayable.payable_amount
        # get the current is_paid status from obj
        current_is_paid = schoolPayable.is_paid

        try:
            # grab the current expense amount from Statement
            schoolPayable_expense_statement = Statement.objects.get(id_of_sector=schoolPayable.id)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection):
                school = request.data.get('school')
                other_school = request.data.get('other_school')
                payable_amount = request.data.get('payable_amount')
                date_of_transaction = request.data.get('date_of_payment')
                schoolPayable_expense_statement = Statement.objects.create(coming_from_sector=school.school_name if school is not None else other_school, amount_of_money=payable_amount,payment_category="School Payable", date_of_transaction=date_of_transaction, bank=bank, id_of_sector=schoolPayable.id)
                schoolPayable_expense_statement.save()
            else:
                pass

        if(bank_connection and payment_bank is not None):
            # compare with coming data from request.data
            if (current_is_paid == False and current_expense_amount == updated_expense_amount):
                # update amount to the bank model amount
                
                bank.amount_of_money = (bank.amount_of_money - current_expense_amount)
                bank.save()
                # schoolPayable_expense_statement.amount_of_money = updated_expense_amount
                # schoolPayable_expense_statement.save()
            elif ( current_is_paid == True and current_expense_amount != updated_expense_amount) :
                bank.amount_of_money = (bank.amount_of_money + current_expense_amount) - updated_expense_amount
                bank.save()
                schoolPayable_expense_statement.amount_of_money = updated_expense_amount
                schoolPayable_expense_statement.save()
            
            else:
                messages.warning(request, 'Please Check again!')
        if (not bank_connection):
            
            bank.amount_of_money = bank.amount_of_money + current_expense_amount
            bank.save()
            schoolPayable_expense_statement.delete()
            messages.success(request, "deleted school payable statement")

        serializer = SchoolPayableSerializer(schoolPayable, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# End of Japan School Payable

# Agent Payable Start
class AgentPayableListView(generics.ListCreateAPIView):
    queryset = AgentPayable.objects.all()
    serializer_class = AgentPayableSerializer

class AgentPayableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentPayable.objects.all()
    serializer_class = AgentPayableSerializer

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return AgentPayable.objects.get(pk=pk)
        except AgentPayable.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        agentPayable = self.get_object()
        updated_expense_amount = int(request.data.get('payable_amount'))
        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
         # get the current is_paid status from obj
        current_is_paid = agentPayable.is_paid
        # assign company payable current amount to a variable
        current_expense_amount = agentPayable.payable_amount

        payment_bank = request.data.get('payment_bank')
        bank = Bank.objects.get(pk=payment_bank)

        try:
            # grab the current expense amount from Statement
            agentPayable_expense_statement = Statement.objects.get(id_of_sector=agentPayable.id)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection):
                agent_name = request.data.get('agent_name')
                payable_amount = request.data.get('payable_amount')
                date_of_transaction = request.data.get('date_of_payment')
                agentPayable_expense_statement=Statement.objects.create(coming_from_sector=agent_name, payment_category="Agent Payable",amount_of_money=payable_amount, date_of_transaction=date_of_transaction, bank=bank, id_of_sector=agent_name.id)
                agentPayable_expense_statement.save()
            else:
                pass
        # getting the linked bank from requested data for updating
        if(bank_connection and payment_bank is not None):
            # compare with coming data from request.data
            if (current_is_paid == False and current_expense_amount == updated_expense_amount):
                # update amount to the bank model amount
                
                bank.amount_of_money = bank.amount_of_money - current_expense_amount 
                bank.save()
                # agentPayable_expense_statement.amount_of_money = updated_expense_amount
                # agentPayable_expense_statement.save()
            # statement created before now want to update it
            elif (current_is_paid == True and current_expense_amount != updated_expense_amount):
                # update amount to the bank model amount
                print("FROM UPDATING NOT MATch")
                bank.amount_of_money = (bank.amount_of_money + current_expense_amount) - updated_expense_amount
                bank.save()
                agentPayable_expense_statement.amount_of_money = updated_expense_amount
                agentPayable_expense_statement.save()
            
            else:
                messages.warning(request, 'Please Check again!')
        else:
            
            bank.amount_of_money = bank.amount_of_money + current_expense_amount
            bank.save()
            # companyPayable_expense_statement.amount_of_money = updated_expense_amount
            agentPayable_expense_statement.delete()
            messages.success(request, "deleted agent payable statement")

        serializer = AgentPayableSerializer(agentPayable, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Agent Payable END


# Employee Payable Start

class EmployeePayableListView(generics.ListCreateAPIView):
    queryset = EmployeePayable.objects.all()
    serializer_class = EmployeePayableSerializer

class EmployeePayableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeePayable.objects.all()
    serializer_class = EmployeePayableSerializer

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return EmployeePayable.objects.get(pk=pk)
        except EmployeePayable.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        employeePayable = self.get_object()

        # get the current salary of employee
        current_salary = employeePayable.salary_amount
        # getting data from request
        updated_salary_amount = int(request.data.get('salary_amount'))
        updated_loan_amount = int(request.data.get('loan_amount'))
        updated_bonus_amount = int(request.data.get('bonus_amount'))
        updated_medical_amount = int(request.data.get('medical_expense'))
        date_of_payment = request.data.get('date_of_payment')
        payment_bank = request.data.get('payment_bank')
        current_employee = request.data.get('employee')

        # getting the paid status from all
        salary_paid_status = request.data.get('salary_paid_status')
        loan_paid_status = request.data.get('loan_paid_status')
        bonus_paid_status = request.data.get('bonus_paid_status')
        medicalExpense_paid_status = request.data.get('medicalExpense_paid_status')

        # bank connection check
        bank_connection = request.data.get('connect_with_bank')
        # get the connected bank
        bank = Bank.objects.get(pk=payment_bank)

        try:
            # grab the current expense amount from Statement
            employeePayable_amount_statement = Statement.objects.get(id_of_sector=employeePayable.id)
        except Statement.DoesNotExist:
            # create Statement for particular expense if bank
            if(bank_connection and salary_paid_status == True):
                # bank = Bank.objects.get(pk=payment_bank)
                # check for more condition
                # creating a new statment for salary with specific employee
                employeePayable_amount_statement=Statement.objects.create(coming_from_sector="Employee Payment", payment_category="salary", paid_to=employeePayable.employee.employee_name, paid_to_id = employeePayable.employee.id, amount_of_money=updated_salary_amount, date_of_transaction=date_of_payment, bank=bank, id_of_sector=employeePayable.id)
                employeePayable_amount_statement.save()
            else:
                pass

        # getting the linked bank from requested data for updating
        payment_bank = int(request.data.get('payment_bank'))

        if(bank_connection and salary_paid_status == True):
            # Write more conditions HERE!!
            if (updated_salary_amount > current_salary):
                # update amount to the bank model amount
                # bank = Bank.objects.get(pk=payment_bank)
                bank.amount_of_money = (bank.amount_of_money + current_salary) - updated_salary_amount
                bank.save()
                employeePayable_amount_statement.amount_of_money = updated_salary_amount
                employeePayable_amount_statement.save()
            else:
                pass
        elif(bank_connection and loan_paid_status==True):
            # check for loan amount
            if (updated_loan_amount > 0):
                bank.amount_of_money = (bank.amount_of_money + employeePayable.loan_amount) - updated_loan_amount
                bank.save()
                employeePayable_amount_statement=Statement.objects.create(coming_from_sector="Employee Loan: "+current_employee.employee_name, amount_of_money=updated_loan_amount, date_of_money_in=date_of_payment, bank=bank, id_of_sector=employeePayable.id)
                employeePayable_amount_statement.save() 
            else:
                messages.warning(request, 'Please Check again!')

        # else:
        #     bank = Bank.objects.get(pk=payment_bank)
        #     bank.amount_of_money = bank.amount_of_money + (current_expense_amount- updated_salary_amount)
        #     bank.save()
        #     # companyPayable_expense_statement.amount_of_money = updated_expense_amount
        #     agentPayable_expense_statement.delete()
        #     messages.success(request, "deleted statement")

        serializer = EmployeePayableSerializer(employeePayable, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Employee Payable END
