from django import forms
from .models import *
from django.forms  import ValidationError
class RegistrationForm(forms.ModelForm):
    GENDER  = (
        ('Male','Male'),
        ('Female','Female')
    )
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    phone = forms.IntegerField()
    
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','phone','gender')
    def clean(self):
        errors=[]
        first_name = self.cleaned_data['first_name']
        phone=self.cleaned_data['phone']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if(password != confirm_password):
            errors.append("Password doesn't match")
        
        if(len(first_name)< 2):
            errors.append("Fistname is too short")
        if(len(username)< 2):
            errors.append("Username is too short")
            
        #if(len(phone)<11):
        #    errors.append("Please enter atleast 10 numbers")

        if(len(errors) > 0):
            raise ValidationError(errors)

    
    def save(self):
        user  = User(username = self.cleaned_data['username'],gender = self.cleaned_data['gender'],first_name = self.cleaned_data['first_name'],last_name= self.cleaned_data['last_name'],phone=self.cleaned_data['phone'],email=self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
