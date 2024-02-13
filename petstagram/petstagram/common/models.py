from django.db import models

# Create your models here.
class ProfilePhotos(models.Model):
    image = models.ImageField(upload_to='profile_photos')
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    # title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    used_currently = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.title