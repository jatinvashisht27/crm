from .models import CV
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = "__all__"
        widgets = {
            'mobID':forms.TextInput(attrs={'class':'form-control'}),
            'group1':forms.TextInput(attrs={'class':'form-control'}),
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'primaryNumber':forms.TextInput(attrs={'class':'form-control'}),
            'primaryMail':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'})
            }
        