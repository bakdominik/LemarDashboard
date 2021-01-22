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
    zgody_właścicieli_działki = models.BooleanField(default=False)
    zmiana_warunków_technicznych = models.BooleanField(default=False)
    decyzja_lokalizacyjna =models.BooleanField(default=False)
    zudp =models.BooleanField(default=False)
    służebność_przesyłu =models.BooleanField(default=False)
    konserwator_zabytków =models.BooleanField(default=False)
    wody_polskie =models.BooleanField(default=False)
    projekt_geotechniczny = models.BooleanField(default=False)
    wejście_w_teren =models.BooleanField(default=False)
    organizacja_ruchu = models.BooleanField(default=False)
    opracowanie_projektu_budowlanego =models.BooleanField(default=False)
    uzgodnienie_projektu_w_PSG =models.BooleanField(default=False)
    uzgodnienie_projektu_u_zarządcy_drogi = models.BooleanField(default=False)
    pozwolenie_na_budowe = models.BooleanField(default=False)
    zaświadczenie_o_nie_wniesieniu_sprzeciwu_wobec_zgłoszenia = models.BooleanField(default=False)
    dziennik_budowy = models.BooleanField(default=False)
    zdjęcie_pasa_drogowego = models.BooleanField(default=False)
    umieszczenie_infrastruktury_technicznej_w_pasie_drogowym = models.BooleanField(default=False)
    wykonanie_robót_w_terenie = models.BooleanField(default=False) 
    szkice_powykonawcze = models.BooleanField(default=False)
    zgłoszenie_zakończenia_budowy_do_PINB = models.BooleanField(default=False)
    zaświadczenie_o_braku_sprzeciwu_wobec_użytkowania = models.BooleanField(default=False)
    project = models.OneToOneField(Project, primary_key=True,on_delete=models.CASCADE)

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