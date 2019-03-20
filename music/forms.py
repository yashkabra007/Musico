from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    # profile_photo = forms.FileField()
    bio = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=25)

    class Meta:
        model = User
        fields = ('username', 'email', 'bio', 'password1', 'password2')
