from django.contrib import admin

from .models import (Task,
                     Project,
                     ProjectContact,
                     Interest,
                     CommunicationInterest)


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'deadline',
        'description',
        'project',
        'interest',
        'routine',
        'regularity',
        'done',
        # 'category',
    )
    list_editable = (
        'name',
        'deadline',
        'deadline',
        'description',
        'project',
        'interest',
        'routine',
        'regularity',
        'done',
        # 'category',
    )
    search_fields = ("name", "description", "pk")
    list_filter = ('deadline',)
    empty_value_display = "-пусто-"


admin.site.register(Task, TaskAdmin)
admin.site.register(Project)
admin.site.register(ProjectContact)
admin.site.register(Interest)
admin.site.register(CommunicationInterest)
