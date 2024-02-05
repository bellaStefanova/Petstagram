from django.urls import path

from .views import register, login, account_home

urlpatterns = [
    path('register', register, name = 'register'),
    path('login', login, name = 'login'),
    path('home', account_home, name = 'account_home')
]
