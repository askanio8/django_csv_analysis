from typing import Type

from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})

    def save(self, commit: bool = True) -> Type["CustomUser"]:  # noqa: FBT001, FBT002
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def form_valid(self, form) -> HttpResponseRedirect:  # noqa: ANN001
        user = form.save()
        login(self.request, user)
        return redirect("home")


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
        self.fields["username"].label = "Email"
        self.fields["password"].widget = forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
        self.fields["password"].label = "Password"

        # Удаляем помощь по паролю, если это необходимо
        self.fields["password"].help_text = None
