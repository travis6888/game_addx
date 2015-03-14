from django import forms
from home.models import Email

__author__ = 'Travis'


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'your@gmail.com'}))

    class Meta:
        model = Email
        fields = {'email'}