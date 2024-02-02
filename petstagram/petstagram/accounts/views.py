from django import http
from django.shortcuts import render

def register(request):
    return http.HttpResponse('Register HTML here')

def login(request):
    return http.HttpResponse('Login HTML here')
