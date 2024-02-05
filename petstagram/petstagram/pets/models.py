from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.URLField()
    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.pk}'
