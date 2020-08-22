from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.views.generic import FormView
from django.contrib.auth.models import User

class ReportAdmin(forms.Form):
	reason =  forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,label="Reason",choices=(("The admin has been inactive for a long time","The admin has been inactive for a long time"),("The admin is unable to resolve issues","The admin is unable to resolve issues"),("The admin has violated the rules and respect of the website","The admin has violated the rules and respect of the website"),("The admin repeatedly askes for removal of users without any valid reason","The admin repeatedly askes for removal of users without any valid reason")),required=True)
	comment = forms.CharField(label="Comment(Optional)",widget = forms.Textarea,required=False)

