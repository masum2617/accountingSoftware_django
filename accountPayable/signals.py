from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from .models import CompanyPayable
from bank.models import Bank, Statement

def less_money_from_bank(current_amount, new_money_in):
    return current_amount - new_money_in

# function to save statment and update bank balance for each expense
def updateStatementForExepenses(modelName, expense_type, price, date_of_payment, payment_bank, bank_id, sector_id):
    modelName.objects.create(coming_from_sector=expense_type, amount_of_money=price, date_of_money_in=date_of_payment, bank=payment_bank, id_of_sector=sector_id)

    bank = Bank.objects.get(id=bank_id)
    bank.amount_of_money= less_money_from_bank(bank.amount_of_money , price)
    bank.save()


@receiver(post_save, sender=CompanyPayable)
def asset_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.payment_bank is not None and instance.connect_with_bank == True:
            updateStatementForExepenses( Statement,instance.company_name, instance.payable_amount,instance.date_of_payment,instance.payment_bank, instance.payment_bank.id, instance.id)