from django.contrib import admin

from .models import Executor, Project, Task

# Register your models here.

admin.site.register([Executor, Project, Task])
