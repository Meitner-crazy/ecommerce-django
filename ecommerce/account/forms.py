from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from django import forms


from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] # PW2 is confirmation

# Allow email to be unique

    # Access to class above?
    def __init__(self, *args, **kwargs):# Keyword arguments
        super(CreateUserForm, self).__init__(*args, **kwargs)

        # Mark email field as required*
        self.fields['email'].required = True


    # Email validation
    def clean_email(self):

        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():

            raise forms.ValidationError('This email is invalid') # The user has signed up already

        if len(email) >= 350:
            raise forms.ValidationError('Your email is too long')
  
        
        return email


# Login form

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())

    password = forms.CharField(widget=PasswordInput())


# Update username and email form

class UpdateUserForm(forms.ModelForm):

    password = None # it's not updated

    class Meta:

        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password1'] # don't wanna make use of these stuff


    def __init__(self, *args, **kwargs):# Keyword arguments
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        # Mark email field as required*
        self.fields['email'].required = True


    # 
    def clean_email(self):

        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():

            raise forms.ValidationError('This email is invalid') # The user has signed up already

        if len(email) >= 350:
            raise forms.ValidationError('Your email is too long')
        
        return email
