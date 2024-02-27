from rest_framework import serializers

from .models import Executor, Project, Task


class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = ["name", "ended_tasks", "id"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title", "id"]


class TaskSerializer(serializers.ModelSerializer):
    executor = serializers.CharField("executor.name")
    projects = ProjectSerializer(read_only=True, many=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "date_created",
            "deadline",
            "executor",
            "priority",
            "title",
            "description",
            "projects",
        ]
