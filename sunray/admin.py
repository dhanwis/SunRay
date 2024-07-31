# admin.py

from django.contrib import admin
from .models import Project
from .models import LargeProject

admin.site.register(LargeProject)
admin.site.register(Project)
