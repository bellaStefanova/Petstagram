from django import forms

from petstagram.accounts.models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
        