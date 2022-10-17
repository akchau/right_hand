from django.contrib import admin

from .models import (Task,
                     Project,
                     ProjectContact,
                     Interest,
                     CommunicationInterest)

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(ProjectContact)
admin.site.register(Interest)
admin.site.register(CommunicationInterest)
