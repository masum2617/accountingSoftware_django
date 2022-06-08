from django.contrib import admin
from .models import PersonalReceivable,CompanyReceivable,JapanSchoolReceivable,StudentReceivable
# Register your models here.


class CompanyReceivableAdmin(admin.ModelAdmin):
    list_display = ['id','company_name','receivable_amount', 'date_of_receive', 'method_of_receive' ]
    
class StudentReceivableAdmin(admin.ModelAdmin):
    list_display = ['student','first_installment_amount', 'second_installment_amount', 'third_installment_amount', 'remaining_installment_amount','total_fees','date_of_receive', 'first_installment_is_receieved' ]

admin.site.register(CompanyReceivable,CompanyReceivableAdmin)
admin.site.register(StudentReceivable, StudentReceivableAdmin)
