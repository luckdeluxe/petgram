"""User forms"""
#Unique Error
from django.db import IntegrityError
#Django
from django import forms

#Models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Sign up form."""
    username = forms.CharField(label=False, min_length=6, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(label=False, max_length=70, widget=forms.PasswordInput(attrs={'placeholder':'Password','class': 'form-control','required': True}))
    password_confirmation = forms.CharField(label=False, min_length=8, widget=forms.PasswordInput(attrs={'placeholder':'Confirm password','class': 'form-control','required': True}))
    first_name = forms.CharField(label=False, min_length=4, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}))
    last_name = forms.CharField(label=False, min_length=4, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}))
    email = forms.CharField(label=False, min_length=6, max_length=50, widget=forms.EmailInput(attrs={'placeholder':'Email','class': 'form-control','required': True}))

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is alredy in use.')
        return username
    
    def clean_email(self):
        """Email must be unique"""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('Email is alredy in use.')
        return email

    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        return data


    def save(self):
        """Save user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

    




class ProfileForm(forms.Form):
    """Profile form"""
    website = forms.URLField(max_length=50, required=True)
    biography = forms.CharField(max_length=200, required=False)
    phone_number = forms.CharField(max_length=13, required=True)
    picture = forms.ImageField()
