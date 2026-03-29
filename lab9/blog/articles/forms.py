from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "text"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Название статьи",
                    "class": "form-input",
                }
            ),
            "text": forms.Textarea(
                attrs={
                    "placeholder": "Текст статьи",
                    "class": "form-textarea",
                    "rows": 10,
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if Article.objects.filter(title__iexact=title).exists():
            raise forms.ValidationError("Статья с таким названием уже существует.")

        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Имя пользователя",
            }
        ),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": "Email",
            }
        ),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Пароль",
            }
        ),
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Повторите пароль",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data["username"].strip()

        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует.")

        return username


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Имя пользователя",
            }
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Пароль",
            }
        ),
    )