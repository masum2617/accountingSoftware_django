from django.contrib import admin
from .models import DailyExpense, UtilityExpense
# Register your models here.

admin.site.register(DailyExpense)
admin.site.register(UtilityExpense)
