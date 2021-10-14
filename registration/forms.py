from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()

class CreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('first_name','last_name','username','email')


#login - вход в аккаунт


class Loginform(forms.Form):
    username= forms.CharField(max_length= 25,label="Enter username")
    password= forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)
