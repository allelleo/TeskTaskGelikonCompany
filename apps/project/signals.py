from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Task


@receiver(post_delete, sender=Task)
def delete_task(sender, instance, **kwargs):
    executor = instance.executor
    executor.ended_tasks += 1
    executor.save()
