import os
from django.conf import settings
from django.urls import reverse
from django.views import generic as views

from petstagram.accounts.models import Account
from .models import Pet
from .forms import AddPetForm

empty_pet_photo = {
    pet_type[0]: os.path.join(settings.STATIC_URL, f'images/{pet_type[0]}_default_photo.jpg') for pet_type in Pet.TYPES_OF_PETS


    # Pet.PET_TYPE_DOG: os.path.join(settings.STATIC_URL, 'images/dog_default_photo.jpg'),
    # 'dog': os.path.join(settings.STATIC_URL, 'images/dog_default_photo.jpg'),
    # 'cat': os.path.join(settings.STATIC_URL, 'images/cat_default_photo.jpg'),
}

class AddPetView(views.FormView):
    template_name = 'pets/add-pet.html'
    form_class = AddPetForm

    def form_valid(self, form):
        request = self.request
        # unique_filename = f"{uuid.uuid4()}{os.path.splitext(request.FILES['image'].name)[1]}"
        # file_path = os.path.join(settings.MEDIA_ROOT, 'profile_photos/', unique_filename)
        # default_storage.save(file_path, ContentFile(request.FILES['image'].read()))
        instance = form.save(commit=False)
        # instance.image = unique_filename
        instance.user = Account.objects.get(username=request.user)
        # for photo in ProfilePhotos.objects.filter(user=instance.user):
        #     photo.used_currently = False
        #     photo.save()
        # instance.used_currently = True
        # instance.user.profile_picture = unique_filename
        # instance.user.save()
        instance.main_image = empty_pet_photo[instance.type]
        instance.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = self.request.method
        return context
   
    def get_success_url(self):
        return reverse('common:account_home')
    
class EditPetView(views.FormView):
    template_name = 'pets/edit-pet.html'
    form_class = AddPetForm
