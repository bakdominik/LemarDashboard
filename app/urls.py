# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path, include
from app import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    # path('project_remove/<int:pk>/', views.project_remove_index, name='project_remove'),
    # path('profile/project_remove/<int:pk>/', views.project_remove_profile, name='project_remove'),
    path('project/<int:pk>/',views.project),
    path('update/<int:pk>/',views.update, name='update'),
    path('check/<int:pk>/',views.check, name='check'),
    path('update_file/<int:pk>/',views.update_file, name='update_file'),
    path('update_invoice/<int:pk>/',views.update_invoice, name='update_invoice'),
    path('', views.index, name='home'),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
