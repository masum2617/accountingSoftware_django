from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from .models import CompanyPayable,PersonalPayable,AgentPayable,EmployeePayable,JapanSchoolPayable
from bank.models import Bank, Statement

def less_money_from_bank(current_amount, new_money_in):
    return current_amount - new_money_in

# function to save statment and update bank balance for each expense
def updateStatementForExepenses(modelName, expense_type,category, price, date_of_payment, payment_bank, bank_id, sector_id):
    modelName.objects.create(coming_from_sector=expense_type,payment_category=category, amount_of_money=price, date_of_transaction=date_of_payment, bank=payment_bank, id_of_sector=sector_id)

    bank = Bank.objects.get(id=bank_id)
    bank.amount_of_money= less_money_from_bank(bank.amount_of_money , price)
    bank.save()


@receiver(post_save, sender=CompanyPayable)
def companyPayable_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.payment_bank is not None and instance.connect_with_bank == True:
            updateStatementForExepenses( Statement,instance.company_name, "Company Payable", instance.payable_amount,instance.date_of_payment,instance.payment_bank, instance.payment_bank.id, instance.id)
        else:
            pass

# Signals for Personal Payable 
@receiver(post_save, sender=PersonalPayable)
def personalPayable_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.payment_bank is not None and instance.connect_with_bank == True:
            updateStatementForExepenses( Statement,instance.person_name, "Personal Payable", instance.payable_amount,instance.date_of_payment,instance.payment_bank, instance.payment_bank.id, instance.id)
        else:
            pass

# Signals for Japan School Payable
@receiver(post_save, sender=JapanSchoolPayable)
def japansShool_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.payment_bank is not None and instance.connect_with_bank == True:
            updateStatementForExepenses( Statement,instance.school.school_name,"Japan School Payable", instance.payable_amount,instance.date_of_payment,instance.payment_bank, instance.payment_bank.id, instance.id)
        else:
            pass

# Signals for Agent Payable
@receiver(post_save, sender=AgentPayable)
def agentPayable_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.payment_bank is not None and instance.connect_with_bank == True:
            updateStatementForExepenses( Statement,instance.agent_name.agent_name,"Agent Payable", instance.payable_amount,instance.date_of_payment,instance.payment_bank, instance.payment_bank.id, instance.id)
        else:
            pass

# signal for employee payable
@receiver(post_save, sender=EmployeePayable)
def EmployeePayable_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.payment_bank is not None and instance.connect_with_bank == True:
            if instance.salary_paid_status == True:
                updateStatementForExepenses( Statement, instance.employee.employee_name,"Employee salary", instance.salary_amount,instance.date_of_payment,instance.payment_bank, instance.payment_bank.id, instance.id)
            if instance.loan_paid_status == True:
                updateStatementForExepenses( Statement,instance.employee.employee_name,"Employee Loan", instance.loan_amount,instance.date_of_payment,instance.payment_bank, instance.payment_bank.id, instance.id)
            if instance.bonus_paid_status == True:
                updateStatementForExepenses( Statement,instance.employee.employee_name,"Employee Bonus", instance.bonus_amount,instance.date_of_payment,instance.payment_bank, instance.payment_bank.id, instance.id)
            if instance.medicalExpense_paid_status == True:
                updateStatementForExepenses( Statement,instance.employee.employee_name,"Employee Medical Expense", instance.medical_expense,instance.date_of_payment,instance.payment_bank, instance.payment_bank.id, instance.id)
        else:
            pass