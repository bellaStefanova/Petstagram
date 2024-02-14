from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import AddPetView, EditPetView

urlpatterns = [
    path('add-pet', AddPetView.as_view(), name = 'add_pet'),
    path('edit-pet', EditPetView.as_view(), name = 'edit_pet'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)