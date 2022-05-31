from django.contrib import admin
from .models import CompanyPayable

# Register your models here.
class CompanyPayableAdmin(admin.ModelAdmin):
    list_display = ['id','company_name','payable_amount', 'date_of_payment', 'method_of_payment' ]


admin.site.register(CompanyPayable,CompanyPayableAdmin)
