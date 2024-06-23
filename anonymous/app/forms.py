
from django import forms
from .models import Message

class Messageform(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message',]