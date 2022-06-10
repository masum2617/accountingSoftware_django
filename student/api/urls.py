from django.urls import path
from .views import StudentListView,StudentDetailView, EducationalRecordDetailView,EducationalRecordListView,EmergencyContactDetailView,EmergencyContactRecordListView

urlpatterns =[
    path('student-list/', StudentListView.as_view(), name='student-list' ),
    path('student-detail/<int:pk>/', StudentDetailView.as_view(), name='student-detail' ),

    path('educational-record/', EducationalRecordListView.as_view(), name='educational-list' ),
    path('educational-record-detail/<int:pk>/', EducationalRecordDetailView.as_view(), name='educational-detail' ),

    path('emergency-contact-list/', EmergencyContactRecordListView.as_view(), name='emergency-list' ),
    path('emergency-contact-detail/<int:pk>/', EmergencyContactDetailView.as_view(), name='emergency-detail' ),
]