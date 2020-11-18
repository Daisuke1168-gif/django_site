from django import forms
from .models import Question,Choice


class ChoiceCreateForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ('votes',)