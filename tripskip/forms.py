from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tripskip.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    phone = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'first_name', 'last_name', 'password1', 'password2', )

class UserUpdateForm(forms.ModelForm):
	class Meta:
		 model = User
		 fields = ['username', 'email', 'first_name', 'last_name', ]

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone',)