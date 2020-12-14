# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from . models import Project, Checklist, ProjectFile, ProjectInvoice

admin.site.register(Project)
admin.site.register(Checklist)
admin.site.register(ProjectFile)
admin.site.register(ProjectInvoice)
# Register your models here.
