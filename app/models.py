# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    W_TRAKCIE = "W"
    ZAKOŃCZONY = "Z"
    PRZERWANY = "P"
    STATUS_CHOICES = [
        (W_TRAKCIE, "W trakcie"),
        (ZAKOŃCZONY, "Zakończony"),
        (PRZERWANY, "Przerwany")
    ]
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    localization = models.CharField(max_length=255,default="Kraków")
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=W_TRAKCIE)
    date_started = models.DateField(auto_now=True)
    value = models.IntegerField()

    def __str__(self):
        return self.title