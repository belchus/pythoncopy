from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
class AddMovie(forms.Form):
 title =  forms.CharField(max_length=40)
 img = forms.CharField(max_length= 250)
 description = forms.CharField(max_length=200)
 tag = forms.CharField(max_length=40)


class AddReview(forms.Form):
   title =  forms.CharField(max_length=40)
   img = forms.CharField(max_length= 250)
   text = forms.CharField(max_length=200)
   user = forms.CharField(max_length=40)
   date = forms.DateField()
   stars = forms.IntegerField()
   avatar = forms.CharField(max_length= 250)



class AddFav(forms.Form):
    title =  forms.CharField(max_length=40)
    stars = forms.IntegerField()
    like = forms.BooleanField()



class FindMovie(forms.Form):
 title = forms.CharField()
 

 class UserCreationForm(UserCreationForm):
    user = forms.CharField(label = 'Username', widget= forms.TextInput(attrs = {'class':'form-input'}))
    email = forms.EmailField(widget= forms.TextInput(attrs = {'class':'form-input'}))
    pass1 = forms.CharField(label = 'Password', widget= forms.PasswordInput(attrs = {'class':'form-input','placeholder': '********'}))
    pass2 = forms.CharField(label = 'Repeat password', widget = forms.PasswordInput(attrs = {'class':'form-input','placeholder': '********'}))
   
class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}