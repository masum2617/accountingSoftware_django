from django.contrib import admin
from .models import DailyExpense, UtilityExpense, MiscExpense, DocumentRenewalExpense, OfficeRentExpense
# Register your models here.


class DocumentRenewalExpenseAdmin(admin.ModelAdmin):
    list_display = ['id','document_name','renewal_amount', 'renewal_date','method_of_payment','payment_bank' ]
    search_fields = ['document_name', 'payment_bank']
    list_display_links= ['id', 'document_name' ]
    list_per_page = 10


admin.site.register(DailyExpense)
admin.site.register(UtilityExpense)
admin.site.register(MiscExpense)
admin.site.register(DocumentRenewalExpense,DocumentRenewalExpenseAdmin)
admin.site.register(OfficeRentExpense)
