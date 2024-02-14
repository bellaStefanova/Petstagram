from django.contrib import admin
from django.urls import include, path, reverse
from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('common:account_home'))
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('', include('petstagram.accounts.urls')),
    path('', include(('petstagram.common.urls', 'common'), namespace='common')),
    path('', include(('petstagram.pets.urls', 'pets'), namespace='pets')),
]

# to create apps photos, pets, common
# common - home page, about page, contact page