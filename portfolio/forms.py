from django import forms
from .models import User


class Registration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'age', 'password', 'messages']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'messages': forms.Textarea(attrs={'class': 'form-control'})
        }
