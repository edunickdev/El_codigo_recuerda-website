from django import forms
from django.forms import ModelForm


class ContactmeForm(ModelForm):
	names = forms.CharField(null=False, blank=False)
	email = forms.EmailField(null=False, blank=False)
	text = forms.CharField(max_length=150, null=False, blank=False)
	
	