# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from . models import Project
from . forms import ProjectForm

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def profile(request):
    projects = Project.objects.filter(user=request.user)
    html_template = loader.get_template( 'profile.html' )

    if request.method == 'POST':
        project = Project()
        project.user = request.user
        project.title = request.POST['title']
        project.localization = request.POST['localization']
        project.date_started = request.POST['datepicker']
        project.status = request.POST['status']
        project.value = request.POST['value']
        project.save()
        return redirect('profile')
    else:
        return HttpResponse(html_template.render({"projects":projects}, request))
    

# @login_required(login_url="/login/")
# def pages(request):

#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:
        
#         load_template      = request.path.split('/')[-1]
#         context['segment'] = load_template
        
#         html_template = loader.get_template( load_template )
#         return HttpResponse(html_template.render(context, request))
        
#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template( 'page-404.html' )
#         return HttpResponse(html_template.render(context, request))

#     except:
    
#         html_template = loader.get_template( 'page-500.html' )
#         return HttpResponse(html_template.render(context, request))



