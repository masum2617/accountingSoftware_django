from django.urls import path
from expenses.api.views import DailyExpenseList
urlpatterns = [

    path('expense_list/',DailyExpenseList.as_view(), name='expense-list')
   
] 
