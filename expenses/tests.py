from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from .models import DailyExpense
from bank.models import Bank

class DailyExpenseTest(APITestCase):

    bank = Bank.objects.get(bank_name='Dhaka Bank')
    print(bank.amount_of_money)

    def test_create_daily_expense(self):
        url = reverse('daily-expense-list')
        data = {
            "expense_type": "Fish",
            "price": 450 + self.bank.amount_of_money,
            "quantity": 5,
            "date_of_payment": "2022-05-23",
            "method_of_payment": "Bank",
            "note": "none",
            "payment_bank": 1
        }
        # print("UPdated money: ", data.price)
        response = self.client.post(url, data,format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
