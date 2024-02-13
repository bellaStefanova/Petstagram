from django.forms import ValidationError
from django.utils import timezone
from django import http
from django.views import generic as views
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from django.urls import reverse, reverse_lazy
from django.contrib import auth


from petstagram.accounts.forms import RegisterForm, LoginForm
from .models import Account


''' this is the Class View for the sign-up page - used in the urls.py file'''
class SignUpView(views.FormView):
    template_name = 'accounts/sign-up.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise http.Http404('You are already logged in')
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_in_header'] = 'index'
        context['method'] = self.request.method
        return context

    def form_valid(self, form):
        user = Account.objects.create_account(
                form.cleaned_data['email'], 
                form.cleaned_data['password'], 
                form.cleaned_data['username'],
                form.cleaned_data['first_name'],
                form.cleaned_data['last_name']
        )
        return redirect(self.get_success_url())
    
        
    def get_success_url(self):
        return reverse_lazy('sign-in')


''' this is the Function View for the sign-up page - not used, just left for reference. 
    It does exactly the same as the Class View above'''
# def sign_up(request):
#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             raise http.Http404('You are already logged in')
#         context = {
#             'account_form': RegisterForm(),
#             'link_in_header': 'index',
#             'method': request.method,
#         }
#         return render(request, 'accounts/sign-up.html', context)
    
#     if request.method == 'POST':
#         account_form = RegisterForm(request.POST)
#         context = {
#             'account_form': account_form,
#             'link_in_header': 'index',
#             'method': request.method,
#         }
#         if account_form.is_valid():
#             try:
#                 user = Account.objects.create_account(
#                     account_form.data['email'], 
#                     account_form.data['password'], 
#                     account_form.data['username'],
#                     account_form.data['first_name'],
#                     account_form.data['last_name'])
                
#                 return http.HttpResponseRedirect('sign-in')
            
#             except ValidationError as e:
#                 return render(request, 'accounts/sign-up.html', context)
#         else:
#             return render(request, 'accounts/sign-up.html', context)

''' this is the Class View for the sign-in page - used in the urls.py file'''
class SignInView(views.FormView):
    template_name = 'accounts/sign-in.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise http.Http404('You are already logged in')
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        request = self.request

        user = Account.objects.get(username=username)
        user.last_login = timezone.now()
        user.save()
        user = auth.authenticate(request, username=username, password=password)
        auth.login(request, user)
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = self.request.method
        return context
   
    def get_success_url(self):
        return reverse('common:account_home')


''' this is the Function View for the sign-up page - not used, just left for reference. 
    It does exactly the same as the Class View above'''

# def sign_in(request):
#     if request.method == 'GET':
#         context = {
#                     'login_form': LoginForm(),
#                     'method': request.method,
#             }
#         return render(request, 'accounts/sign-in.html', context)
    
#     if request.method == 'POST':

#         login_form = LoginForm(request.POST)
#         context = {
#                 'login_form': login_form,
#                 'method': request.method,
#         }
#         username = request.POST['username']
#         password = request.POST['password']

#         try:
#             user = Account.objects.get(username=username)
#             if check_password(password, user.password):
#                 user.last_login = timezone.now()
#                 user.save()
#                 user = auth.authenticate(request, username=username, password=password)
#                 auth.login(request, user)
#                 return redirect(reverse('common:account_home'))
#             else:
#                 login_form.add_error('password', 'Incorrect password')
#                 return render(request, 'accounts/sign-in.html', context)
#         except Exception as e:
#             login_form.add_error('username', 'User with this name does not exist')
#             return render(request, 'accounts/sign-in.html', context)

def sign_out(request):
    auth.logout(request)
    return redirect(reverse('index'))

