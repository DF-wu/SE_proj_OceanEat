#-*- encoding: utf-8 -*-
from django import forms

# Create your tests here.

class LoginForm(forms.Form):
	username = forms.CharField(label='帳號', max_length=50)
	password = forms.CharField(label='密碼', widget=forms.PasswordInput())
	