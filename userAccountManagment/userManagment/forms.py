from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Имя пользователя'}))
    password1 = forms.CharField(required=True, label='Пароль', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(required=True, label='Повторите пароль', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'пароль'}))
    email = forms.EmailField(required=True, error_messages='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
