from django import forms
from . import models

class NameForm(forms.Form):
    Event_name = forms.CharField(label='Event Name', max_length=25)
    Event_location = forms.CharField(label='Event Location',max_length=15)
    Event_Org = forms.CharField(label='Organization',max_length=15)
    #Event_host = forms.ForeignKey(models.Event_Users, on_delete=forms.CASCADE)
    Event_start_date = forms.DateTimeField()
    Event_end_date = forms.DateTimeField()