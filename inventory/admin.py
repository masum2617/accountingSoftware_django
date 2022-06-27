from django.contrib import admin
from .models import Asset
# Register your models here.

class AssetAdmin(admin.ModelAdmin):
    list_display = ['id','asset_name','asset_price']

admin.site.register(Asset, AssetAdmin)