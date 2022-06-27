from django.contrib import admin
# from .models import Student, EducationalRecord,EmergencyContact
from .models import Student, EducationalRecord

class EducationalRecordAdmin(admin.ModelAdmin):
    list_display = ['id','student' ]

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','student_name','student_id' ]

admin.site.register(Student,StudentAdmin)
admin.site.register(EducationalRecord, EducationalRecordAdmin)
# admin.site.register(EmergencyContact)
