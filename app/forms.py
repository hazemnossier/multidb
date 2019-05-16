from django import forms
from django.forms import ModelForm
from .models import SQLData


class fill_me_form(ModelForm):
    class Meta:
        model = SQLData
        fields = ['fill_me']
