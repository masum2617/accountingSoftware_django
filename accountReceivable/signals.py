from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from .models import CompanyReceivable,JapanSchoolReceivable,PersonalReceivable,StudentReceivable
from bank.models import Bank, Statement
from .helper import calculate_remaining_amount

def add_money_to_bank(current_amount, new_money_in):
    return current_amount + new_money_in


# function to save statment and update bank balance for each expense
def updateStatementForReceivable(modelName, received_from, category, receivable_amount, date_of_receive, received_bank, received_by, bank_id, sector_id):
    modelName.objects.create(coming_from_sector=received_from, payment_category=category, amount_of_money=receivable_amount, date_of_transaction=date_of_receive, received_by= received_by, bank=received_bank, id_of_sector=sector_id)

    bank = Bank.objects.get(id=bank_id)
    bank.amount_of_money= add_money_to_bank(bank.amount_of_money , receivable_amount)
    bank.save()

# signals for company receivable
@receiver(post_save, sender=CompanyReceivable)
def receivable_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.received_bank is not None and instance.connect_with_bank == True:
            updateStatementForReceivable( Statement,instance.company_name, "Company Receivable", instance.receivable_amount,instance.date_of_receive,instance.received_bank, instance.received_by, instance.received_bank.id, instance.id)
        else:
            pass


# signal for personal 

@receiver(post_save, sender=PersonalReceivable)
def receivable_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.received_bank is not None and instance.connect_with_bank == True:
            updateStatementForReceivable( Statement,instance.person_name, "Personal Receivable", instance.receivable_amount,instance.date_of_receive,instance.received_bank, instance.received_by, instance.received_bank.id, instance.id)
        else:
            pass



# signal for Japan School 
@receiver(post_save, sender=JapanSchoolReceivable)
def receivable_post_save(sender,instance, created, **kwargs):
    if created:
        if instance.received_bank is not None and instance.connect_with_bank == True:
            updateStatementForReceivable( Statement,instance.person_name, "Japan School Receivable", instance.receivable_amount,instance.date_of_receive,instance.received_bank, instance.received_by, instance.received_bank.id, instance.id)
        else:
            pass


@receiver(pre_save, sender=StudentReceivable)
def student_receivable_pre_save(sender, instance, *args, **kwargs):
    if instance.remaining_installment_amount == 0:
        instance.remaining_installment_amount = calculate_remaining_amount(instance.total_fees, instance.first_installment_amount, instance.second_installment_amount,instance.third_installment_amount)

# signal for Student Recevable for creating statement
@receiver(post_save, sender=StudentReceivable)
def student_receivable_post_save(sender,instance, created, **kwargs):
    if created:
        # if only first installment paid
        if (instance.first_installment_amount > 0 and instance.second_installment_amount == 0 and instance.third_installment_amount == 0 and instance.received_bank is not None and instance.connect_with_bank == True):
            updateStatementForReceivable( Statement,instance.student.student_name, "Student Receivable", instance.first_installment_amount,instance.date_of_receive,instance.received_bank, instance.received_by, instance.received_bank.id, instance.id)

        elif (instance.first_installment_amount > 0 and instance.second_installment_amount > 0 and instance.third_installment_amount == 0 and instance.received_bank is not None and instance.connect_with_bank == True):
            updateStatementForReceivable( Statement,instance.student.student_name, "Student Receivable", instance.second_installment_amount,instance.date_of_receive,instance.received_bank, instance.received_by, instance.received_bank.id, instance.id)

        elif (instance.first_installment_amount > 0 and instance.second_installment_amount > 0 and instance.third_installment_amount > 0 and instance.received_bank is not None and instance.connect_with_bank == True):
            updateStatementForReceivable( Statement,instance.student.student_name, "Student Receivable", instance.third_installment_amount,instance.date_of_receive,instance.received_bank, instance.received_by, instance.received_bank.id, instance.id)

        elif(instance.is_full_paid == True and instance.received_bank is not None and instance.connect_with_bank == True):
            updateStatementForReceivable( Statement,instance.student.student_name, "Student Receivable", instance.total_fees,instance.date_of_receive,instance.received_bank, instance.received_by, instance.received_bank.id, instance.id)
            


