from django import http
from django.db import IntegrityError
from django.shortcuts import render

from petstagram.accounts.forms import AccountForm, LoginForm
from petstagram.accounts.models import Account
from petstagram.accounts.exceptions import EmailExistsError, InvalidEmailFormat, PasswordError

def register(request):
    if request.method == 'GET':
        print('get')
        context = {
            'account_form': AccountForm(),
        }
        return render(request, 'accounts/register.html', context)
    
    if request.method == 'POST':
        account_form = AccountForm(request.POST)
        try:
            user = Account.objects.create_user(account_form.data['email'], account_form.data['password'], account_form.data['username'])
            return http.HttpResponseRedirect('login')
        except EmailExistsError as e:
            return render(request, 'accounts/register.html', {'account_form': account_form})
        except InvalidEmailFormat as e:
            return render(request, 'accounts/register.html', {'account_form': account_form})
        except PasswordError as e:
            account_form.add_error('password', e)
            return render(request, 'accounts/register.html', {'account_form': account_form})


def login(request):
    if request.method == 'GET':
        print('get')
        context = {
                    'login_form': LoginForm(),
            }
        return render(request, 'accounts/login.html', context)
    
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        email = login_form.data['email']
        password = login_form.data['password']
        user = Account.objects.get(email=email)
        if not user:
            login_form.add_error('email', 'User does not exist')
            return render(request, 'accounts/login.html', {'login_form': login_form})
