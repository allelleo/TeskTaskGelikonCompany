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
    executor = serializers.CharField(source="executor.name")
    projects = ProjectSerializer(read_only=True, many=True)

    def create(self, validated_data):
        request = self.context["request"]
        projects = request.data.get("projects")
        print(projects)
        for i in projects:
            print(i, type(i))
        projects = [Project.objects.get(pk=i) for i in projects]
        validated_data["projects"] = projects
        instance = super().create(validated_data)

        return instance

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
