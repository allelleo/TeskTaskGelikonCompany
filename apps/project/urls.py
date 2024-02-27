from django.urls import path

from .views import TaskDetail, TaskList, delete_task

urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
    path("<int:pk>/", TaskDetail.as_view(), name="task-detail"),
    path("/destroy", delete_task),
]
