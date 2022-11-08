from django import forms

from .models import User
class UserForm(forms.Form):
    id=forms.IntegerField()
    name=forms.CharField()
    dateOfBirth=forms.DateField()

class UserModelForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

