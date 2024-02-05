from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('', include('petstagram.accounts.urls')),
]

# to create apps photos, pets, common
# common - home page, about page, contact page