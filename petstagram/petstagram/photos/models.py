from django.db import models

# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(upload_to='images')
    description = models.TextField(validators=[models.MaxLengthValidator(300), models.MinLengthValidator(10)],
                                   blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    pets = models.ManyToManyField('pets.Pet', related_name='photos')
    date_of_publication = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField('comments.Comment', related_name='photos')
    likes = models.ManyToManyField('likes.Like', related_name='photos')
    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pet.name} - {self.pk}'