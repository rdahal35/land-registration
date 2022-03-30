from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserForm(forms.ModelForm):
    password1 = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "password",
                  "password1", "email", "public_address"]
