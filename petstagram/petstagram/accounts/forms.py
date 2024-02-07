from django import forms

from petstagram.accounts.models import Account

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'password', )
        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'username': None,
        }
        labels = {
            'email': 'Email',
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

        