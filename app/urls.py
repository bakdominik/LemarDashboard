# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from django.conf.urls import url

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    # path('project_remove/<int:pk>/', views.project_remove_index, name='project_remove'),
    # path('profile/project_remove/<int:pk>/', views.project_remove_profile, name='project_remove'),
    path('project/<int:pk>/',views.project),
    path('', views.index, name='home'),


]
