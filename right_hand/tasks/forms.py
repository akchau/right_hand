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
            'description',
            'deadline',
            'project',
            'routine',
            'regularity',
            'plan_pomodoro',
        )

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['regularity'].required = False


class TaskFormWithProject(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'name',
            'deadline',
            'description',
            'routine',
            'regularity',
            'plan_pomodoro',
        )


class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = (
            'name',
            'revenue',
            'partner',
            'main_contact',
        )


class InterestFormWithPartner(forms.ModelForm):
    class Meta:
        model = Interest
        fields = (
            'name',
            'revenue',
            'main_contact',
        )
