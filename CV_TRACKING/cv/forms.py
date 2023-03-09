from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from .models import Company


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cd = super().clean()
        username = cd.get("username")
        password = cd.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError("Wrong data. Please try again.")


class CompanyForm(forms.ModelForm):
    name = forms.CharField()
    work_position= forms.CharField()

    class Meta:
        model = Company
        fields = ('name', 'work_position')


class ApplicationForm(forms.ModelForm):

    class Meta:
        fields = ['company', 'post_date', 'position', 'salary', 'reply', 'reply_date', 'other']

