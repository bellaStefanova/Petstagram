import os
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from petstagram.accounts.models import Account
from .models import Pet

empty_pet_photo = {
    pet_type[0]: os.path.join(settings.STATIC_URL, f'images/{pet_type[0]}_default_photo.jpg') for pet_type in Pet.TYPES_OF_PETS
}

class AddPetView(views.CreateView):
    model = Pet
    template_name = 'pets/add-pet.html'
    fields = ['name', 'type', 'short_info', 'date_of_birth']
    success_url = reverse_lazy('common:account_home')

    def form_valid(self, form):
        request = self.request
        instance = form.save(commit=False)
        instance.user = Account.objects.get(username=request.user)
        instance.main_image = empty_pet_photo[instance.type]
        instance.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = self.request.method
        return context

    
class EditPetView(views.TemplateView):
    template_name = 'pets/edit-pet.html'
    success_url = reverse_lazy('common:account_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet'] = Pet.objects.get(pk=kwargs['pk'])
        return context

class EditPetDetailsView(views.UpdateView):
    template_name = 'pets/edit-pet-details.html'
    model = Pet
    fields = ['name', 'type', 'short_info', 'date_of_birth']
    success_url = reverse_lazy('common:account_home')

class ViewPetView(views.DetailView):
    model = Pet
    template_name = 'pets/view-pet.html'
    context_object_name = 'pet'

    
class DeletePetView(views.DeleteView):
    model = Pet
    template_name = 'pets/delete-pet.html'
    success_url = reverse_lazy('common:account_home')
