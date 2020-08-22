from django import forms

class AddIssue(forms.Form):
	description = forms.CharField(label='Description',max_length = 200)
