from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	username = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'User Name'}))
	email = forms.EmailField(label="",required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	password1 = forms.CharField(label="",required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>')
	password2 = forms.CharField(label="",required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Comfirm Password'}),help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>')

	class Meta:
		model = User
		fields = ('username','email', 'password1', 'password2')

