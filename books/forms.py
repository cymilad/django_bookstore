from django import forms
from .models import *

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
