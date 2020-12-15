from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import template
from . models import Project, Checklist, ProjectFile, ProjectInvoice
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db.models.functions import TruncMonth
from django.db.models.aggregates import Count, Sum
from django.utils.dateformat import DateFormat
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

@login_required(login_url="/login/")
def index(request):
    projects = Project.objects.all()
    html_template = loader.get_template( 'index.html' )

    # New project chart
    new_labels, new_data = get_chart_data(Project,5,Count('month'))
    # Sales chart
    sales_labels, sales_data = get_chart_data(Project,7,Sum('value'))

    user_active = len(Project.objects.filter(user=request.user,status='W trakcie'))
    user_all = len(Project.objects.filter(user=request.user))

    if request.method == 'POST':
        return add_project(request,'home')
    return HttpResponse(html_template.render({"projects":projects,"new_labels":new_labels,"new_data":new_data, "sales_labels":sales_labels,"sales_data":sales_data,'user_active':user_active,'user_all':user_all}, request))

@login_required(login_url="/login/")
def profile(request):
    projects = Project.objects.filter(user=request.user)
    html_template = loader.get_template( 'profile.html' )
    
    if request.method == 'POST':
        return add_project(request,'profile')
    else:
        return HttpResponse(html_template.render({"projects":projects}, request))

@login_required(login_url="/login/")
def project(request,pk):
    project = Project.objects.get(pk=pk)
    files = ProjectFile.objects.filter(project=pk)
    invoices = ProjectInvoice.objects.filter(project=pk)
    html_template = loader.get_template( 'project.html' )
    return HttpResponse(html_template.render({"project":project,"files":files,"invoices":invoices}, request))



@login_required(login_url="/login/")
def update(request,pk):
    if request.method == "POST":
        project = Project.objects.get(pk=pk)
        project.user = request.user
        project.title = request.POST['title']
        project.localization = request.POST['localization']
        project.date_started = request.POST['datepicker'].format('YYYY-MM-DD')
        project.status = request.POST['status']
        project.value = request.POST['value']
        project.project_object = request.POST['project_object']
        project.investor = request.POST['investor']
        project.save()
        return redirect('/project/'+str(pk))

@login_required(login_url="/login/")
def update_file(request,pk):
    if request.method == "POST":
        project_file = ProjectFile()
        project_file.title = request.POST['file_title']
        project_file.file = request.FILES['file']
        project_file.project = Project.objects.get(pk=pk)
        project_file.save()
        return redirect('/project/'+str(pk))

@login_required(login_url="/login/")
def update_invoice(request, pk):
    if request.method == "POST":
        invoice = ProjectInvoice()
        invoice.title = request.POST['invoice_title']
        invoice.invoice = request.FILES['invoice']
        invoice.project = Project.objects.get(pk=pk)
        invoice.status = request.POST['status']
        invoice.save()
        return redirect('/project/'+str(pk))

@login_required(login_url="/login/")
def update_invoice_status(request, pk):
    if request.method == "POST":
        invoice = ProjectInvoice.objects.get(pk=pk)
        invoice.status = request.POST['status']
        invoice.save()
        return redirect('/project/'+str(invoice.project.pk))


@login_required(login_url="/login/")
def check(request,pk):
    if request.method == "POST":
        project = Project.objects.get(pk=pk)
        checklist = project.checklist
        setattr(checklist, request.POST['checked'], True)
        checklist.save()
        return redirect('/project/'+str(pk))

@login_required(login_url="/login/")
def settings(request):
    user_active = len(Project.objects.filter(user=request.user,status='W trakcie'))
    user_finished = len(Project.objects.filter(user=request.user,status='Zakończony'))
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Hasło zostało zmienione')
        else:
            return render(request, 'settings.html',{'user_active':user_active,'user_finished':user_finished,'form':form})

    form = PasswordChangeForm(request.user)

    html_template = loader.get_template( 'settings.html' )
    return HttpResponse(html_template.render({'user_active':user_active,'user_finished':user_finished,'form':form},request))

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
    checklist = Checklist()
    checklist.project = project
    checklist.save()
    return redirect(url)


def get_chart_data(Model,months_before,aggregation):
    now = datetime.utcnow()
    from_datetime = now - relativedelta(months=months_before-1)
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

def project_pdf(request,pk):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    doc = SimpleDocTemplate(buffer)
    flowables = []
    style = getSampleStyleSheet()
    paragraph_1 = Paragraph("A title", style['Heading1'])
    paragraph_2 = Paragraph(
    "Some normal body text",
    style['BodyText']
    )
    flowables.append(paragraph_1)
    flowables.append(paragraph_2)
    doc.build(flowables)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    buffer = buffer.getvalue()


    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="some_file.pdf"'
    
    response.write(buffer)
    return response
    # return FileResponse(buffer, as_attachment=True, filename='hello.pdf')