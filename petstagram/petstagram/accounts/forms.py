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

    def is_valid(self):
        if self.data['email'] == '':
            self.add_error('email', 'Please enter an email address')
        if ' ' in self.data['username'] and 'username' not in self.errors:
            self.add_error('username', 'Username cannot contain spaces')
        if self.data['first_name'] == '':
            self.add_error('first_name', 'Please enter your first name')
        if self.data['last_name'] == '':
            self.add_error('last_name', 'Please enter your last name')
        return super().is_valid()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

        