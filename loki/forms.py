from django import forms

from users.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=4, max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'username', 'placeholder': 'Username or email'
    }))

    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'id': 'password', 'placeholder': 'Password'
    }))

class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=4, max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'username', 'placeholder': 'Username'
    }))

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
        'class': 'form-control', 'id': 'email', 'placeholder': 'Email'
    }))

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'id': 'password', 'placeholder': 'Contraseña'
    }))

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )