from django import forms
from .models import ProfilePhotos


class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = ProfilePhotos
        fields = ['image', 'description']
        widgets = {
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

        