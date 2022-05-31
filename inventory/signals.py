from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib import messages
from django.utils.text import slugify

from .models import Asset
from bank.models import Bank, Statement

def less_money_from_bank(current_amount, new_money_in):
    return current_amount - new_money_in

# function to save statment and update bank balance for each expense
def updateStatementForExepenses(modelName, expense_type, price, date_of_payment, payment_bank, bank_id):
    modelName.objects.create(coming_from_sector=expense_type, amount_of_money=price, date_of_money_in=date_of_payment, bank=payment_bank)

    bank = Bank.objects.get(id=bank_id)
    bank.amount_of_money= less_money_from_bank(bank.amount_of_money , price)
    bank.save()

@receiver(pre_save, sender=Asset)
def asset_pre_save(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.asset_name)

@receiver(post_save, sender=Asset)
def asset_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.payment_bank is not None and instance.is_paid == True:
            updateStatementForExepenses( Statement,instance.asset_name, instance.asset_price,instance.purchase_date,instance.payment_bank, instance.payment_bank.id)