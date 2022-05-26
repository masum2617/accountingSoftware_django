from django.urls import path
from expenses.api.views import DailyExpenseList, DailyExpenseDetail

urlpatterns = [
    path('daily-expense/',DailyExpenseList, name='daily-expense-list'),
    path('daily-expense/<int:pk>/',DailyExpenseDetail, name='daily-expense'),
    # path('daily-expense/',DailyExpenseList.as_view(), name='daily-expense-list'),
    # path('daily-expense/<int:pk>/',DailyExpenseDetail.as_view(), name='daily-expense'),
   
] 
