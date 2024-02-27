from django.db import models

# Create your models here.


class Executor(models.Model):
    name = models.CharField(max_length=200)


class Project(models.Model):
    title = models.CharField(max_length=60)


class Task(models.Model):
    HIGH_PRIORITY = 3
    MEDIUM_PRIORITY = 2
    LOW_PRIORITY = 1

    PRIORITY_CHOICES = (
        (HIGH_PRIORITY, "High"),
        (MEDIUM_PRIORITY, "Medium"),
        (LOW_PRIORITY, "Low"),
    )
    date_created = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    executor = models.ForeignKey(Executor, on_delete=models.SET_NULL, null=True)
    priority = models.IntegerField(max_length=1, choices=PRIORITY_CHOICES)

    title = models.CharField(max_length=60)
    description = models.TextField()
    projects = models.ManyToManyField(Project)
