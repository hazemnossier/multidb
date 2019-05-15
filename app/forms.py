from django import forms
from django.forms import ModelForm
from .models import Data


class fill_me_form(ModelForm):
    class Meta:
        model = Data
        fields = ['fill_me']
