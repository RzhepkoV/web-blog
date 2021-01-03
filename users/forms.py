from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label = 'Введите E-mail',
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите E-mail'})
    )
    username = forms.CharField(
        label = 'Введите логин',
        required=True,
        help_text = 'Обязательное поле. Не более 150 символов. Нельзя вводить символы: @, /, _',
        max_length = 150,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label = 'Введите пароль',
        required=True,
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        label = 'Подтвердите пароль',
        required=True,
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'})
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
    label = 'Имя пользователя*',
    required=True,
    help_text = 'Обязательное поле. Не более 150 символов. Нельзя вводить символы: @, /,_',
    max_length = 150,
    widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    email = forms.EmailField(
        label = 'E-mail*',
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите E-mail'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label = 'Изменить',
        required=False,
        widget = forms.FileInput
    )


    class Meta:
        model = Profile
        fields = ['img']

class GenderPlusAcceptForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Выберете пол*',
        required=False,
        choices = Profile.gen,
        widget = forms.Select(attrs={'class': 'custom-select'})

    )
    accept = forms.BooleanField(
        label= 'Соглашение на отправку уведомлений на почту',
        required = False,
        widget = forms.CheckboxInput(attrs={'class': 'custom-checkbox'})
    )

    class Meta:
        model = Profile
        fields = ['gender', 'accept']
