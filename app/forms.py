from django import forms


class ProjectForm(forms.Form):
    name = forms.CharField(max_length=255)
    title = forms.CharField(max_length=255)
    localization = forms.CharField(max_length=255)
    status = forms.CharField()
    datepicker = forms.DateField()
    value = forms.IntegerField()