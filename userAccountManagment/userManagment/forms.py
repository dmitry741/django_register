from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Имя пользователя'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'пароль'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'пароль'}))
    email = forms.EmailField(required=True, error_messages='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'email'}))
    #first_name = forms.BooleanField(disabled=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        #fields = ('__all__')