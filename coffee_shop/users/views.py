from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class RegisterView(generic.CreateView):
    template_name = "users/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")