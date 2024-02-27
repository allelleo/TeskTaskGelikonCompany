from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view

from .models import Executor, Project, Task
from .serializers import ExecutorSerializer, ProjectSerializer, TaskSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(["DELETE"])
def delete_task(request):
    task_id = request.data.get("task_id")
    task = Task.objects.get(pk=task_id)
    executor = task.executor
    executor.ended_tasks += 1
    executor.save()
    task.delete()
    return JsonResponse({"status": "ok"})
