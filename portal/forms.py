from django import forms
from django.core.validators import RegexValidator
from .models import User, UserProfile

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Например: student123'
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'example@mail.ru'
            }
        )
    )

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }
        )
    )

    password_confirm = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль'
            }
        )
    )

    full_name = forms.CharField(
        label='ФИО',
        validators=[
            RegexValidator(
                regex=r'^[А-Яа-яЁё\s]+$',
                message='ФИО должно содержать только кириллицу и пробелы'
            )
        ],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Иванов Иван Иванович'
            }
        )
    )

    phone = forms.CharField(
        label='Телефон',
        validators=[
            RegexValidator(
                regex=r'^8\(\d{3}\)\d{3}-\d{2}-\d{2}$',
                message='Телефон в формате 8(XXX)XXX-XX-XX'
            )
        ],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '8(900)123-45-67'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'phone']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            self.add_error('password_confirm', "Пароли не совпадают")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                full_name=self.cleaned_data['full_name'],
                phone=self.cleaned_data['phone']
            )
        return user
