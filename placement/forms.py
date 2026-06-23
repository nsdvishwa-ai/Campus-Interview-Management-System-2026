from django import forms
from .models import Student, Company


class StudentRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = '__all__'


class StudentLoginForm(forms.Form):
    reg_no = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'