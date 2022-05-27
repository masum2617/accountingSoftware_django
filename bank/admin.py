from django.contrib import admin
from .models import Bank, Statement
# Register your models here.

class BankAdmin(admin.ModelAdmin):
    list_display = ['id','bank_name','bank_branch', 'amount_of_money' ]
    search_fields = ['bank_name', 'bank_branch']
    list_display_links= ['id', 'bank_name' ]
    list_per_page = 10

    list_filter = ()

admin.site.register(Bank,BankAdmin)
admin.site.register(Statement)
