from django.urls import path

from .views import account_home, view_profile

urlpatterns = [
    path('home/', account_home, name = 'account_home'),
    path('my-profile/', view_profile, name = 'view_profile'),
]