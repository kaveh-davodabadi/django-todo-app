from django import forms


from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "add here a new task"})
    )
    is_completed = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    class Meta:
        model = Task
        fields = "__all__"
