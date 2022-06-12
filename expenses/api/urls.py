from django.urls import path
from expenses.api.views import DailyExpenseList, DailyExpenseDetail,DocumentRenewalExpenseList,DocumentRenewalExpenseDetail,OfficeRentExpenseDetail,OfficeRentExpenseList,MiscExpenseList,MiscExpenseDetail,UtilityExpenseList,UtilityExpenseDetail

urlpatterns = [
    path('daily-expense/',DailyExpenseList.as_view(), name='daily-expense-list'),
    path('daily-expense-detail/<int:pk>/',DailyExpenseDetail.as_view(), name='daily-expense'),

    path('utility-expense/',UtilityExpenseList.as_view(), name='utility-expense-list'),
    path('utility-expense-detail/<int:pk>/',UtilityExpenseDetail.as_view(), name='utility-expense'),

    path('office-rent/',OfficeRentExpenseList.as_view(), name='office-rent-list'),
    path('office-rent-detail/<int:pk>/',OfficeRentExpenseDetail.as_view(), name='office-rent-detail'),
    
    path('document-renewal/',DocumentRenewalExpenseList.as_view(), name='document-renewal-list'),
    path('document-renewal-detail/<int:pk>/',DocumentRenewalExpenseDetail.as_view(), name='document-renewal-detail'),

    path('miscellaneous-expenses/',MiscExpenseList.as_view(), name='miscellaneous-expenses-list'),
    path('miscellaneous-expenses-detail/<int:pk>/',MiscExpenseDetail.as_view(), name='miscellaneous-expenses-detail'),
   
] 
