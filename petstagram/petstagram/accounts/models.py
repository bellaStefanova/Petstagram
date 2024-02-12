from django.contrib.auth.models import User, UserManager
from django.db import models
from .validators import (
    FirstNameValidator, 
    LastNameValidator, 
    EmailValidator, 
    UsernameValidator, 
    PasswordValidator)


class AccountManager(UserManager):
    def create_account(self, email, password, username, first_name, last_name, **extra_fields):

        user = self.model(email = email,
                          password = password,
                          username = username,
                          first_name = first_name,
                          last_name = last_name,
                          **extra_fields)

        user.full_clean()

        return super().create_user(
            email=email, 
            password=password, 
            username=username, 
            first_name=first_name, 
            last_name=last_name,
            **extra_fields)
    

class Account(User):

    pets = models.ManyToManyField('pets.Pet', blank=True)
    profile_picture = models.ImageField(upload_to="static/images", null=True, blank=True)

    objects = AccountManager()


    def __init__(self, *args, **kwargs):

        emails=[x['email'] for x in Account.objects.all().values('email')]
        super(Account, self).__init__(*args, **kwargs)
        self._meta.get_field('first_name').validators = [FirstNameValidator()]
        self._meta.get_field('last_name').validators = [LastNameValidator()]
        self._meta.get_field('email').validators = [EmailValidator(emails)]
        self._meta.get_field('username').validators = [UsernameValidator()]
        self._meta.get_field('password').validators = [PasswordValidator()]
        
