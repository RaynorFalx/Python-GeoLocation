from django import forms
from .models import *

class TargetForm(forms.Form):
    target_id = forms.CharField()
