from django.contrib import admin
from django.contrib.admin import register
from .models import Task

# Register your models here.


@register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "is_completed"]
    list_editable = ["is_completed"]
