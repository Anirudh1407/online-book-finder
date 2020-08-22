from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.views.generic import FormView
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.layout import Submit


class RegisterForm(UserCreationForm):
	gender = forms.ChoiceField(choices=(('M','Male'),('F','Female'),('O','Other'),))
	name = forms.CharField()
	email = forms.EmailField()
	dob = forms.DateField(
		widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
	)
	country = forms.CharField()
	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_action = reverse('register')
		self.helper.add_input(Submit('submit', 'REGISTER', css_class='btn-dark'))
	class Meta:
		model = User
		fields = ['username','name','email','gender','dob','country','password1','password2']

class ReportUser(forms.Form):
	reason =  forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,label="Reason",choices=(("The user repeatedly reports issues when nothing is wrong","The user repeatedly reports issues when nothing is wrong"),("The user has put up questionable content","The user has put up questionable content"),("The user has violated the rules and respect of the website","The user has violated the rules and respect of the website")),required=True)
	comment = forms.CharField(label="Comment(Optional)",widget = forms.Textarea,required=False)


class ProfileChange(forms.Form):
	gender = forms.ChoiceField(choices=(('M','Male'),('F','Female'),('O','Other'),),label="Gender")

	email = forms.EmailField(label="Email")
	dob = forms.DateField(label = "DOB")
	country = forms.CharField(label="Country")
	def __init__(self, *args, **kwargs):
		super(ProfileChange, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Change Profile'))



	
