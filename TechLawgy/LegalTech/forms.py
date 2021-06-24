from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cases

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
'email', 'password1', 'password2',)



class RegisterCases(forms.ModelForm):
    # specify the name of model to use
    
    payee_name = forms.CharField(max_length=100, help_text='Payee Name')

    class Meta:
        model = Cases
        exclude = ('user_name',)
        