from django.shortcuts import render
from django import http

from petstagram.accounts.models import Account

def account_home(request):
    return render(request, 'common/account_home.html')
    # return http.HttpResponse('to do account home page')

def view_profile(request):
    username = request.user
    user = Account.objects.get(username=username)
    context= {
        'profile': user,
        'full_name': user.get_full_name(),
        'profile_picture': user.profile_picture or 'images/add-profile-picture.jpg',
    }
    return render(request, 'common/view-profile.html', context)
    