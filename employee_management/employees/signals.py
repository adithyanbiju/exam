from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Employee

@receiver(pre_save, sender=Employee)
def uppercase_employee_name(sender, instance, **kwargs):
    if instance.name:
        instance.name = instance.name.upper()
