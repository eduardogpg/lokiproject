from django import forms
from django.core.exceptions import ValidationError

from users.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=4, max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none', 
            'id': 'username', 
            'placeholder': 'Username'
    }))

    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none', 
            'id': 'password', 
            'placeholder': 'Password'
    }))


class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=4, max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
        'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none', 
        'id': 'username', 
        'placeholder': 'Username'
    }))

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
        'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none', 
        'id': 'email', 
        'placeholder': 'Email'
    }))

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none', 
            'id': 'password', 
            'placeholder': 'Contraseña'
    }))

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise ValidationError("El username ya se encuentra en uso.")
        
        return username


    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise ValidationError("El email ya se encuentra en uso.")
        
        return email

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )