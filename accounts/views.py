from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView
# Create your views here.

class SignUp(CreateView):
	template_name = "accounts/signup.html"
	form_class = forms.UserForm
	success_url = reverse_lazy("login")
    

