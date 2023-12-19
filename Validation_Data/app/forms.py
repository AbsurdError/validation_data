from django import forms

class InputName(forms.Form):
    name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-field', 'name': 'name'}))

class InputEmail(forms.Form):
    email = forms.EmailField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-field', 'name': 'email'}))

class InputPassword(forms.Form):
    password = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-field', 'name': 'password'}))