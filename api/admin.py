from django.contrib import admin
from .models import Bug, Enroll,Project,Task
admin.site.register(Enroll)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Bug)
