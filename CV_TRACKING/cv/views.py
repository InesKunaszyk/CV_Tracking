from django.shortcuts import render

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.views.generic import FormView, View, CreateView

from .forms import LoginForm, CompanyForm, ApplicationForm
from .models import Company, Application

User = get_user_model()


class Login(FormView):
    template_name = 'cv/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('landing_page')

    def form_valid(self, form):
        cd = form.cleaned_data
        username = cd.get("username")
        password = cd.get("password")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class Logout(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

