from django import forms
from .models import Minutes, Meeting, Agenda, Document

class Minuteform(forms.ModelForm):
    class Meta:
        model = Minutes
        fields = ['textfield',]

        widgets = {'textfield':forms.Textarea()}


class Meetingform(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['name','theme', 'dateScheduled']

        widgets = {
            'dateScheduled': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['title',]

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['docname','doc',]
