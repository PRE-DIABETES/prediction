from django import forms
from .models import *
from django.forms  import ValidationError
class RegistrationForm(forms.ModelForm):
   
    username = forms.CharField()
    email = forms.EmailField()
   
    
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username','email')
    def clean(self):
        errors=[]
        
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if(password != confirm_password):
            errors.append("Password doesn't match")
        
        if(len(username)< 2):
            errors.append("Username is too short")
            
        #if(len(phone)<11):
        #    errors.append("Please enter atleast 10 numbers")

        if(len(errors) > 0):
            raise ValidationError(errors)

    
    def save(self):
        user  = User(username = self.cleaned_data['username'],email=self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
