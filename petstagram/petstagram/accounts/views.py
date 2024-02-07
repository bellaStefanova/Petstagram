from django.utils import timezone
from django import http
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.contrib import auth


from petstagram.accounts.forms import RegisterForm, LoginForm
from petstagram.accounts.models import Account
from petstagram.accounts.exceptions import (
        EmailExistsError, 
        InvalidEmailFormat, 
        PasswordError,
        FirstNameError,
        LastNameError,)

def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            print('test')
            raise http.Http404('You are already logged in')
        context = {
            'account_form': RegisterForm(),
            'link_in_header': 'index',
        }
        return render(request, 'accounts/register.html', context)
    
    if request.method == 'POST':
        account_form = RegisterForm(request.POST)
        context = {
            'account_form': account_form,
            'link_in_header': 'index',
        }
        try:
            user = Account.objects.create_user(
                account_form.data['email'], 
                account_form.data['password'], 
                account_form.data['username'],
                account_form.data['first_name'],
                account_form.data['last_name'])
            
            return http.HttpResponseRedirect('login')
        except EmailExistsError as e:
            return render(request, 'accounts/register.html', context)
        except InvalidEmailFormat as e:
            return render(request, 'accounts/register.html', context)
        except PasswordError as e:
            account_form.add_error('password', e)
            return render(request, 'accounts/register.html', context)
        except FirstNameError as e:
            account_form.add_error('first_name', e)
            return render(request, 'accounts/register.html', context)
        except LastNameError as e:
            account_form.add_error('last_name', e)
            return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'GET':
        context = {
                    'login_form': LoginForm(),
            }
        return render(request, 'accounts/login.html', context)
    
    if request.method == 'POST':

        login_form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Account.objects.get(username=username)
            if check_password(password, user.password):
                user.last_login = timezone.now()
                user.save()
                user = auth.authenticate(request, username=username, password=password)
                auth.login(request, user)
                print(request.user)
                return redirect(reverse('common:account_home'))
            else:
                login_form.add_error('password', 'Incorrect password')
                return render(request, 'accounts/login.html', {'login_form': login_form})
        except Exception as e:
            login_form.add_error('username', 'User with this name does not exist')
            return render(request, 'accounts/login.html', {'login_form': login_form})

