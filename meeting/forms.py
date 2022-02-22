from django import forms
from .models import Minutes

class Minuteform(forms.ModelForm):
    class Meta:
        model = Minutes
        fields = ['textfield',]

        widgets = {'textfield':forms.Textarea()}