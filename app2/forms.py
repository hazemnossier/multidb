from django import forms
from django.forms import ModelForm
from .models import MongoData


class fill_me_form(ModelForm):
    class Meta:
        model = MongoData
        fields = ['fill_me']
