from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Заголовок')
    description = forms.CharField(max_length=3000, required=False, label='Описание', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Статус', initial=default_status)
    date = forms.DateField(required=False, label='дата выполнения', widget=forms.DateInput(attrs={'type': 'date'}))
