# from django.db import models

# class Account(models.Model):
#     username = models.CharField(max_length=30)
#     email = models.EmailField()
#     password = models.CharField(max_length=30)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.username

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from petstagram.accounts.exceptions import EmailExistsError, InvalidEmailFormat, PasswordError


class AccountManager(BaseUserManager):
    def create_user(self, email, password, name, **extra_fields):
        try:
            self.validate_email(email)
            self.validate_password(password)
        except Exception as e:
            raise e
        
        if Account.objects.filter(email=email).exists():
            raise EmailExistsError()
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, username=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def validate_email(self, email):
        if Account.objects.filter(email=email).exists():
            raise EmailExistsError()
        else:
            try:
                email = self.normalize_email(email)
            except ValueError as e:
                raise InvalidEmailFormat()            
            if '@' not in email or '.' not in email:
                raise InvalidEmailFormat()
            else:
                mail_name, domain, tld = email.split('@')[0], email.split('@')[1].split('.')[0], email.split('@')[1].split('.')[1]
                if len(mail_name) < 3 or len(domain) < 3 or len(tld) < 2:
                    raise InvalidEmailFormat()
    
    def validate_password(self, password):
        if len(password) < 8:
            raise PasswordError('Password must be at least 8 characters long')
        elif not any(char.isdigit() for char in password):
            raise PasswordError('Password must contain at least one digit')
        elif not any(char.isupper() for char in password):
            raise PasswordError('Password must contain at least one uppercase letter')
        elif not any(char.islower() for char in password):
            raise PasswordError('Password must contain at least one lowercase letter')
        else:
            return True
    
class Account(AbstractBaseUser):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Add other fields as needed

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'