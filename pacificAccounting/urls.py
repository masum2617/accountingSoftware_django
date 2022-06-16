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
    path('account-receivable/', include('accountReceivable.api.urls')),
    path('student/', include('student.api.urls')),
    path('employees/', include('employee.api.urls')),
    path('services/', include('services.api.urls')),
    path('messages/', include('drf_messages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
