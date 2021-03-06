from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib import messages
from django.forms import ValidationError

from .models import DailyExpense, DocumentRenewalExpense, OfficeRentExpense, UtilityExpense, MiscExpense
from bank.models import Statement, Bank

def less_money_from_bank(current_amount, new_money_in):
    return current_amount - new_money_in

# function to save statment and update bank balance for each expense
def updateStatementForExepenses(modelName, expense_type, price,category, date_of_payment, payment_bank, bank_id):
    modelName.objects.create(coming_from_sector=expense_type, amount_of_money=price, payment_category= category,date_of_transaction=date_of_payment, bank=payment_bank)

    bank = Bank.objects.get(id=bank_id)

    bank.amount_of_money= less_money_from_bank(bank.amount_of_money , price)
    bank.save()


""" Saving money trace for every expenses into Bank Statement Model """
@receiver(post_save, sender=DailyExpense)
def dailyExpense_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.payment_bank is not None and instance.connect_with_bank == True:
            #save money trace in the statement model for future trace
            updateStatementForExepenses( Statement,instance.expense_type, instance.price, "Daily Expense",instance.date_of_payment,instance.payment_bank, instance.payment_bank.id)


@receiver(post_save, sender=UtilityExpense)
def utilityExpense_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.payment_bank is not None and instance.connect_with_bank == True:
            updateStatementForExepenses( Statement,instance.utility_category, instance.monthly_bill,"Utility Expense", instance.date_of_payment,instance.payment_bank, instance.payment_bank.id)


@receiver(post_save, sender=DocumentRenewalExpense)
def dailyExpense_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.payment_bank is not None and instance.connect_with_bank == True:
            #save money trace in the statement model for future trace
            updateStatementForExepenses( Statement,instance.document_name, instance.renewal_amount,"Document Renewal Expense",instance.renewal_date,instance.payment_bank, instance.payment_bank.id)

@receiver(post_save, sender=OfficeRentExpense)
def dailyExpense_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.payment_bank is not None and instance.connect_with_bank == True:
            #save money trace in the statement model for future trace
            updateStatementForExepenses( Statement,instance.expense_type, instance.monthly_cost,"Office Rent Expense",instance.date_of_payment,instance.payment_bank, instance.payment_bank.id)

@receiver(post_save, sender=MiscExpense)
def dailyExpense_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.payment_bank is not None and instance.connect_with_bank == True:
            #save money trace in the statement model for future trace
            updateStatementForExepenses( Statement,instance.expense_name, instance.price,"Miscellaneous Expense",instance.date_of_payment,instance.payment_bank, instance.payment_bank.id)