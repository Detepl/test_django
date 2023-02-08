from .models import User
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["name","pasw"]
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "login",
            }),
            "pasw": TextInput(attrs={
                "class": "form-control",
                "placeholder": "password",
            })
        }
