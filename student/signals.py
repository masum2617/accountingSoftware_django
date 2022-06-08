from django.dispatch import receiver
from django.db.models.signals import pre_save
import uuid
from .models import Student

def random_studentID():
    student_id = str(uuid.uuid4().int)
    return student_id[:6]

@receiver(pre_save, sender=Student)
def receivable_pre_save(sender, instance, *args, **kwargs):
    if instance.student_id is None:
        instance.student_id = random_studentID()
