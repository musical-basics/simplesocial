from django.shortcuts import render
from django.utils import timezone
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (View, TemplateView,
                                ListView, DetailView,
                                CreateView, UpdateView,
                                DeleteView)
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'