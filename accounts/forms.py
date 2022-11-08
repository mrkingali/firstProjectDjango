from django import forms


class RegisterUserForm(forms.Form):
    userName=forms.CharField(max_length=15)
    emailAdress=forms.EmailField()
    password=forms.CharField()
    firstName=forms.CharField()
    lastName=forms.CharField()
class LoginUserForm(forms.Form):
    userName=forms.CharField()
    password=forms.CharField()
