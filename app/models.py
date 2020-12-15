# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
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
    date_started = models.DateField()
    value = models.IntegerField()
    comments = GenericRelation(Comment)
    investor = models.CharField(max_length=600)
    project_object = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

class Checklist(models.Model):

    zlecenie_z_gazowni = models.BooleanField(default=False)
    warunki_techniczne = models.BooleanField(default=False)
    wypis_i_wyrys = models.BooleanField(default=False)
    mapa = models.BooleanField(default=False)
    zup = models.BooleanField(default=False)
    uzyskanie_zgod = models.BooleanField(default=False)
    project = models.OneToOneField(Project, primary_key=True, on_delete=models.CASCADE)

class ProjectFile(models.Model):
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file = models.FileField(upload_to="media/project_files/")



class ProjectInvoice(models.Model):
    OPŁACONY = "O"
    DO_OPŁACENIA = "D"
    STATUS_CHOICES = [
        (OPŁACONY, "Opłacony"),
        (DO_OPŁACENIA, "Do opłacenia"),
    ]
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=DO_OPŁACENIA)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    invoice = models.FileField(upload_to="media/invoices/")