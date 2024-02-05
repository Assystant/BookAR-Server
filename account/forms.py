from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    """
    A form for creating new users. Includes an additional email field.
    """
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class PwdChangeForm(UserCreationForm):
    """
    A form for changing the password of a user. Does not include an email field.
    """
    class Meta:
        model = User
        fields = ('password1', 'password2', )