from django import newforms as forms
from django.newforms.widgets import *
from django.core.mail import send_mail, BadHeaderError

# A simple contact form with four fields.
class RegistrationForm(forms.Form):
	name = forms.CharField(max_length=200)
	email = forms.CharField(max_length=200)
	affiliation = forms.CharField(max_length=200)
	video = forms.CharField(max_length=200)
    acceptance = forms.IntegerField(default=0)