from django.contrib import admin
from .models import Student, EducationalRecord,EmergencyContact
# Register your models here.

admin.site.register(Student)
admin.site.register(EducationalRecord)
admin.site.register(EmergencyContact)
