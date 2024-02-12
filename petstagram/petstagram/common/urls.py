from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import account_home, view_profile

urlpatterns = [
    path('home/', account_home, name = 'account_home'),
    path('my-profile/', view_profile, name = 'view_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)