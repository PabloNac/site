from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Usuario
from .form import UserForm
from django import forms

class home(TemplateView):
    
    template_name = 'App_site/home.html'

class RegisterView(CreateView):
    template_name = 'App_site/Usuario_form.html'
    form_class = UserForm # Usando sua UserForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return redirect('home')