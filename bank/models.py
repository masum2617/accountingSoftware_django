from django.db import models

# Create your models here.
class Bank(models.Model):
    bank_name = models.CharField(max_length=50)
    bank_branch = models.CharField(max_length=50, null=True)
    account_num = models.BigIntegerField()
    amount_of_money = models.BigIntegerField()

    def __str__(self):
        return self.bank_name