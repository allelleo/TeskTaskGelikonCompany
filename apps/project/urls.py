from django.urls import path

from .views import TaskDetail, TaskList

urlpatterns = [
    path("read/", TaskList.as_view(), name="task-list"),
    path("read/<int:pk>/", TaskDetail.as_view(), name="task-detail"),
]
