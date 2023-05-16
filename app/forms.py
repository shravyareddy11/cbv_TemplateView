from app.models import *
from django import forms
class Studentform(forms.ModelForm):
    class Meta():
        model=Student
        fields='__all__'