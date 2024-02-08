from django.forms import ValidationError
from django.utils import timezone
from django import http
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.contrib import auth


from petstagram.accounts.forms import RegisterForm, LoginForm
from .models import Account


def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            raise http.Http404('You are already logged in')
        context = {
            'account_form': RegisterForm(),
            'link_in_header': 'index',
            'method': request.method,
        }
        return render(request, 'accounts/register.html', context)
    
    if request.method == 'POST':
        account_form = RegisterForm(request.POST)
        context = {
            'account_form': account_form,
            'link_in_header': 'index',
            'method': request.method,
        }
        if account_form.is_valid():
            try:
                user = Account.objects.create_account(
                    account_form.data['email'], 
                    account_form.data['password'], 
                    account_form.data['username'],
                    account_form.data['first_name'],
                    account_form.data['last_name'])
                
                return http.HttpResponseRedirect('login')
            
            except ValidationError as e:
                return render(request, 'accounts/register.html', context)
        else:
            return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'GET':
        context = {
                    'login_form': LoginForm(),
                    'method': request.method,
            }
        return render(request, 'accounts/login.html', context)
    
    if request.method == 'POST':

        login_form = LoginForm(request.POST)
        context = {
                'login_form': login_form,
                'method': request.method,
        }
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Account.objects.get(username=username)
            if check_password(password, user.password):
                user.last_login = timezone.now()
                user.save()
                user = auth.authenticate(request, username=username, password=password)
                auth.login(request, user)
                return redirect(reverse('common:account_home'))
            else:
                login_form.add_error('password', 'Incorrect password')
                return render(request, 'accounts/login.html', context)
        except Exception as e:
            login_form.add_error('username', 'User with this name does not exist')
            return render(request, 'accounts/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))
