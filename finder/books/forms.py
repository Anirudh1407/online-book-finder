from django import forms
from crispy_forms.helper import FormHelper
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.layout import Submit

class SearchForm(forms.Form):
    search = forms.CharField(label = '' ,max_length=200)


class AddBook(forms.Form):
	book_name = forms.CharField(label = 'Title',max_length = 200, required= True)
	book_author = forms.CharField(label = 'Authors',max_length = 20, required= True, widget=forms.TextInput(attrs={'placeholder': 'Author1,Author2,...'}))
	book_edition = forms.IntegerField(label = 'Edition', min_value=1,required = True)
	book_link = forms.URLField(label = 'Link', required = True,widget=forms.TextInput(attrs={'placeholder': 'Enter the complete URL'}))
	book_tags = forms.CharField(label = 'Tags',max_length = 20, required = False,widget=forms.TextInput(attrs={'placeholder': 'tag1,tag2,...'}))
	book_image = forms.ImageField(label = 'Image',required = False)

	def __init__(self, *args, **kwargs):
		super(AddBook, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_action = reverse('addbook')
		self.helper.add_input(Submit('submit', 'OK', css_class='btn-light'))  

class AddIssue(forms.Form):
	description = forms.CharField(label='Description',max_length = 200)




