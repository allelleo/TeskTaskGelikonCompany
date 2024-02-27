from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Executor, Project, Task
from .serializers import ExecutorSerializer, ProjectSerializer, TaskSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
