from django import forms

from .models import Project, Task, Interest


class ProjectForm(forms.ModelForm):
    """Форма для создания проекта."""
    class Meta:
        model = Project
        fields = (
            "name",
            "revenue",
            "deadline",
            "my_role",
            "customer"
        )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'name',
            'deadline',
            'project',
        )


class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = (
            'name',
            'revenue',
            'partner',
        )


class InterestFormWithPartner(forms.ModelForm):
    class Meta:
        model = Interest
        fields = (
            'name',
            'revenue',
        )
