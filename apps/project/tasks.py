import datetime

from core.celery import app

from .models import Task


@app.task
def deleting_overdue_tasks():
    tasks = Task.objects.all()
    for task in tasks:
        if task.deadline < datetime.datetime.now():
            executor = task.executor
            executor.ended_tasks += 1
            executor.save()
            task.delete()
