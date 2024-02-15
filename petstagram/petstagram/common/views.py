import os
from django.conf import settings
from django.shortcuts import render
from django import http
from django.urls import reverse
from django.views import generic as views
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import uuid
from django.db.models import Q

from petstagram.accounts.models import Account
from petstagram.pets.models import Pet
from .models import ProfilePhotos
from .forms import ProfilePhotoForm

def account_home(request):
    return render(request, 'common/account_home.html')
    # return http.HttpResponse('to do account home page')



def view_profile(request):
    username = request.user
    user = Account.objects.get(username=username)
    context= {
        'profile': user,
        'full_name': user.get_full_name(),
        'pets': Pet.objects.filter(user=user),
        'profile_picture': os.path.join(settings.MEDIA_URL, 'profile_photos/', user.profile_picture) if 
        user.profile_picture else os.path.join(settings.STATIC_URL, 'images/add-profile-picture.jpg'),
    }
    return render(request, 'common/view-profile.html', context)


class AddProflePictureView(views.FormView):
    template_name = 'common/add-profile-picture.html'
    form_class = ProfilePhotoForm
    
    def form_valid(self, form):
        request = self.request
        unique_filename = f"{uuid.uuid4()}{os.path.splitext(request.FILES['image'].name)[1]}"
        file_path = os.path.join(settings.MEDIA_ROOT, 'profile_photos/', unique_filename)
        default_storage.save(file_path, ContentFile(request.FILES['image'].read()))
        instance = form.save(commit=False)
        instance.image = unique_filename
        instance.user = Account.objects.get(username=request.user)
        for photo in ProfilePhotos.objects.filter(user=instance.user):
            photo.used_currently = False
            photo.save()
        instance.used_currently = True
        instance.user.profile_picture = os.path.join(settings.MEDIA_URL, 'profile_photos/', unique_filename)
        instance.user.save()
        instance.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = self.request.method
        return context
   
    def get_success_url(self):
        return reverse('common:account_home')
    
class SearchView(views.ListView):
    template_name = 'common/search.html'
    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_picture'] = os.path.join(settings.MEDIA_URL, 'profile_photos/', self.model.objects.get(username=self.request.user).profile_picture)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        queryset = queryset.filter(Q(username__icontains=self.request.GET.get('q', None)) |
                                   Q(first_name__icontains=self.request.GET.get('q', None)) |
                                   Q(last_name__icontains=self.request.GET.get('q', None)))
        return queryset
    

# to do
# def upload_profile_picture(request):
#     if request.method == 'GET':
#         pass
#     elif request.method == 'POST': 
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = Account.objects.get(username=request.user)
#             user.profile_picture = form.cleaned_data['image']
#             user.save()
#             return redirect(reverse('common:view_profile'))

    