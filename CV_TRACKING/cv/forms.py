from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

from .models import Company, Application


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

    class Meta:
        model = Company
        fields = ('name', 'work_position')


class ApplicationForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    position = forms.ModelChoiceField(queryset=Company.objects.all())

    class Meta:
        model = Application
        fields = ('company', 'position', 'post_date', 'salary', 'reply', 'reply_date', 'other')
        widgets = {
            'post_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'reply_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }


class UpdateApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('company', 'post_date', 'position', 'salary', 'reply', 'reply_date', 'other')



