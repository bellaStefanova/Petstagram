from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import AddProflePictureView, account_home, view_profile, SearchView

urlpatterns = [
    path('home/', account_home, name = 'account_home'),
    path('my-profile/', view_profile, name = 'view_profile'),
    path('add-profile-picture', AddProflePictureView.as_view(), name = 'add_profile_picture'),
    path('search/', SearchView.as_view(), name = 'search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)