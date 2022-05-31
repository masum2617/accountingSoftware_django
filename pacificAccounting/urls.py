from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expense/', include('expenses.api.urls')),
    path('bank/', include('bank.api.urls')),
    path('inventory/', include('inventory.api.urls')),
    path('account-payable/', include('accountPayable.api.urls')),
    path('messages/', include('drf_messages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
