from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import AddPetView, EditPetView, EditPetDetailsView, ViewPetView, DeletePetView

urlpatterns = [
    path('add-pet', AddPetView.as_view(), name = 'add_pet'),
    path('view-pet/<int:pk>/', ViewPetView.as_view(), name = 'view_pet'),
    path('edit-pet/<int:pk>/', EditPetView.as_view(), name = 'edit_pet'),
    path('edit-pet-details/<int:pk>/', EditPetDetailsView.as_view(), name = 'edit_pet_details'),
    path('delete-pet/<int:pk>/', DeletePetView.as_view(), name = 'delete_pet'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)