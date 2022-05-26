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
            "note": "none"
        }
        # print("UPdated money: ", data.price)
        response = self.client.post(url, data,format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_daily_expense(self, pk):
        daily_exp = DailyExpense.objects.get(pk=pk)
        print(daily_exp)
        
        # url = reverse('daily-expense')
        
        data = {
           
            "expense_type": "Fish",
            "price": 650 + self.bank.amount_of_money,
            "quantity": 5,
            "date_of_payment": "2022-05-23",
            "method_of_payment": "Bank",
            "note": "none"
        }
        # response = self.client.put(url, data,format='json')
        # print("data : ", data)
        # request = self.client.put('daily-expense/1/', data,format='json')
        # print(request)
        # self.assertEqual(request.status_code, status.HTTP_200_OK)
       
