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
    executor = serializers.CharField(source="executor.name", read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)

    def create(self, validated_data):
        request = self.context["request"]

        executor = Executor.objects.get(name=request.data.get("executor"))
        projects = [Project.objects.get(pk=i) for i in request.data.get("projects")]

        validated_data["projects"] = projects
        validated_data["executor"] = executor

        instance = super().create(validated_data)

        return instance

    def update(self, instance, validated_data):
        instance.deadline = validated_data.get("deadline", instance.deadline)
        if validated_data.get("executor", False):
            executor = Executor.objects.get(name=validated_data.get("executor"))
            instance.executor = executor
        instance.priority = validated_data.get("priority", instance.priority)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)

        print(isinstance(validated_data.get("projects"), list))
        print(validated_data.get("projects"))
        if isinstance( validated_data.get("projects"), list):
            projects = [
                Project.objects.get(pk=i) for i in validated_data.get("projects")
            ]
            instance.projects.clear()
            for project in projects:
                print(f"add project: {project.title}")
                instance.projects.add(project)
                instance.save()

        instance.save()
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
