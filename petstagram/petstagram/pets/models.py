from django.db import models

# Create your models here.

class Pet(models.Model):
    TYPES_OF_PETS = (
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('reptile', 'Reptile'),
        ('fish', 'Fish'),
        ('rabbit', 'Rabbit'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=TYPES_OF_PETS)
    short_info = models.TextField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    # photo = models.ImageField(blank=True, null=True)
    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    main_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.type}'

class PetImages(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    image = models.URLField(blank=True, null=True)
    description = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.pet.name} - {self.pet.type} - {self.description}'