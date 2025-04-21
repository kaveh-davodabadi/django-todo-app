from django.urls import path
from .views import index, update_task, delete_task

urlpatterns = [
    path("", index, name="index"),
    path("update-task/<str:pk>/", update_task, name="update-task"),
    path("delete-task/<str:pk>/", delete_task, name="delete-task"),
]
