from django.contrib import admin

from .models import (Task,
                     Project,
                     ProjectContact,
                     Interest,
                     CommunicationsInterest)

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(ProjectContact)
admin.site.register(Interest)
admin.site.register(CommunicationsInterest)
