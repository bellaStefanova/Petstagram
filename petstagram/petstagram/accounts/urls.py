from django.urls import path

from .views import sign_out, SignUpView, SignInView

urlpatterns = [
    path('sign-up', SignUpView.as_view(), name = 'sign-up'),
    path('sign-in', SignInView.as_view(), name = 'sign-in'),
    path('sign-out', sign_out, name = 'sign-out'),
]
