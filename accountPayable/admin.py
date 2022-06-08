from django.contrib import admin
from .models import CompanyPayable,PersonalPayable,AgentPayable,EmployeePayable,JapanSchoolPayable

# Register your models here.
class CompanyPayableAdmin(admin.ModelAdmin):
    list_display = ['id','company_name','payable_amount', 'date_of_payment', 'method_of_payment' ]

class PersonalPayableAdmin(admin.ModelAdmin):
    list_display = ['id','person_name','payable_amount', 'date_of_payment', 'method_of_payment' ]

class JapanSchoolPayableAdmin(admin.ModelAdmin):
    list_display = ['id','other_school','payable_amount', 'date_of_payment', 'method_of_payment' ]

class AgentPayableAdmin(admin.ModelAdmin):
    list_display = ['id','agent_name','payable_amount', 'date_of_payment', 'method_of_payment' ]


admin.site.register(AgentPayable,AgentPayableAdmin)
admin.site.register(EmployeePayable)
admin.site.register(JapanSchoolPayable,JapanSchoolPayableAdmin)
admin.site.register(CompanyPayable,CompanyPayableAdmin)
admin.site.register(PersonalPayable,PersonalPayableAdmin)

