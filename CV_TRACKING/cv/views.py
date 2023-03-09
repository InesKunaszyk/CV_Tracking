from django.shortcuts import render

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.views.generic import FormView, View, CreateView, UpdateView

from .forms import LoginForm, CompanyForm, ApplicationForm, UpdateApplicationForm
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


class LandingPage(LoginRequiredMixin, View):
    template_name = 'cv/landing_page.html'

    def get(self, request, *args, **kwargs):
        cv = Application.objects.all()[::5]
        return render(request, self.template_name, {'cv':cv})


class AddCompany(LoginRequiredMixin, FormView):
    template_name = 'cv/new_company.html'
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy("landing_page")
    login_url = 'login'
    permission_denied_message = 'Aby dodać firmę musisz być zalogowany.'

    def form_valid(self, form):
        cd = form.cleaned_data
        name = cd.get("name")
        work_position = cd.get("work_position")
        Company.objects.create(name=name, work_position=work_position)

        return super().form_valid(form)


class AddApplication(LoginRequiredMixin, FormView):
    template_name = 'cv/new_application.html'
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy("landing_page")
    login_url = 'login'
    permission_denied_message = 'Aby dodać CV musisz być zalogowany.'

    def form_valid(self, form):
        cd = form.cleaned_data
        company = cd.get("company ")
        post_date = cd.get("post_date")
        position = cd.get("position")
        salary = cd.get("salary")
        reply = cd.get("reply")
        reply_date = cd.get("reply_date")
        other = cd.get("other")

        user = User.objects.get(username=self.request.user.username)

        Application.objects.create(user=user,
                                   copmany=company,
                                   post_date=post_date,
                                   position=position,
                                   salary=salary,
                                   reply=reply,
                                   reply_date=reply_date,
                                   other=other)

        return super().form_valid(form)


class UpdateApplication(LoginRequiredMixin, UpdateView):
    template_name = 'cv/update.html'
    model = Application
    form_class = UpdateApplicationForm
    success_url = reverse_lazy('dashboard')


