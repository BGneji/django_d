from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите логин'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Укажите email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Укажите возраст'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Это имя пользователя уже занято.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise forms.ValidationError("Email не может быть пустым.")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже занят.")
        return email

    def clean_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        repeat_password = cleaned_data.get("password2")

        if password != repeat_password:
            raise forms.ValidationError("Пароли не совпадают.")
