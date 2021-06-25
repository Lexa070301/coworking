from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, PasswordInput

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        # widgets = {
        #     "username": TextInput(attrs={
        #         'class': 'form-control common-input',
        #         'placeholder': 'Имя'
        #     }),
        #     "password1": PasswordInput(attrs={
        #         'class': 'form-control common-input',
        #         'placeholder': 'Пароль'
        #     }),
        #     "password2": PasswordInput(attrs={
        #         'class': 'form-control common-input',
        #         'placeholder': 'Повторите пароль'
        #     })
        # }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username',)