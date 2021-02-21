from django import forms
from . models import *
from django.forms import ModelForm

class Results(ModelForm):
    class Meta:
        model = TeerResult
        fields = '__all__'
        #widgets = {
            #'date' : forms.DateInput(attrs={'type':'date'})
       # }