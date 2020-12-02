from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from . models import Project
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db.models.functions import TruncMonth
from django.db.models.aggregates import Count, Sum
from django.utils.dateformat import DateFormat


@login_required(login_url="/login/")
def index(request):
    projects = Project.objects.all()
    html_template = loader.get_template( 'index.html' )

    # New project chart

    new_labels, new_data = get_chart_data(Project,5,Count('month'))

    # Sales chart

    sales_labels, sales_data = get_chart_data(Project,7,Sum('value'))

    if request.method == 'POST':
        return add_project(request,'home')
    return HttpResponse(html_template.render({"projects":projects,"new_labels":new_labels,"new_data":new_data, "sales_labels":sales_labels,"sales_data":sales_data}, request))

@login_required(login_url="/login/")
def profile(request):
    projects = Project.objects.filter(user=request.user)
    html_template = loader.get_template( 'profile.html' )
    
    if request.method == 'POST':
        return add_project(request,'profile')
    else:
        return HttpResponse(html_template.render({"projects":projects}, request))

@login_required()
def project_remove_index(request, pk):
    if request.method =="POST":
        project = Project.objects.filter(pk=pk)
        project.delete()
    return redirect('home')

@login_required()
def project_remove_profile(request, pk):
    if request.method =="POST":
        project = Project.objects.filter(pk=pk)
        project.delete()
    return redirect('profile')

@login_required(login_url="/login/")
def pages(request):

    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

# utils

def add_project(request,url):
    project = Project()
    project.user = request.user
    project.title = request.POST['title']
    project.localization = request.POST['localization']
    project.date_started = request.POST['datepicker'].format('Y-m-d')
    project.status = request.POST['status']
    project.value = request.POST['value']
    project.save()
    return redirect(url)


def get_chart_data(Model,months_before,aggregation):
    now = datetime.utcnow()
    from_datetime = now - relativedelta(months=months_before)
    modified_from_datetime = from_datetime.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    aggregated = Model.objects.filter(date_started__gte=modified_from_datetime).annotate(month=TruncMonth('date_started')).values('month').annotate(sum=aggregation)

    monthsShort = {'1':"Sty",'2':"Lu",'3':"Mar",'4':"Kw",'5':"Maj",'6':"Cze",'7':"Lip",'8':"Sie",'9':"Wrz",'10':"Pa",'11':"Lis",'12':"Gru"} 
    keys = []
    for i in range(months_before):
        if modified_from_datetime.month+i<13:
            keys.append(monthsShort[f'{modified_from_datetime.month+i}'])
        else:
            keys.append(monthsShort[f'{(modified_from_datetime.month+i)%12}'])

    data = {key: 0 for key in keys}

    for project in aggregated:
        data[monthsShort[f'{project["month"].month}']]=project['sum']

    return (list(data.keys()),list(data.values()))

