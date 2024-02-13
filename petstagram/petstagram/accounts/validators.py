from django.forms import ValidationError
import string

ALLOWED_USERNAME_CHARACTERS = set(string.ascii_letters + string.digits + '_.-')


class FirstNameValidator:

    def __init__(self):
        pass
    
    def clean(self, x):
        return x.strip()
    
    def __call__(self, value):

        cleaned = self.clean(value).split()
        
        for name in cleaned:

            if not name.isalpha():
                raise ValidationError('First name must contain only letters')
            
        if len(value) < 2:
            raise ValidationError('First name must be at least 2 characters long')
        
class LastNameValidator(FirstNameValidator):
    
    def __call__(self, value):

        cleaned = self.clean(value)

        if not cleaned.isalpha():
            raise ValidationError('Last name must contain only letters')
        
        if len(cleaned) < 2:
            raise ValidationError('Last name must be at least 2 characters long')
        
class EmailValidator:

    def __init__(self, emails):
        self.existing_emails = emails
    
    def clean(self, x):
        return x.strip()
    
    def __call__(self, value):

        cleaned = self.clean(value)
        
        try:
            mail_name, domain, tld = cleaned.split('@')[0], cleaned.split('@')[1].split('.')[0], cleaned.split('@')[1].split('.')[1]
        except IndexError:
            raise ValidationError('Invalid email format')
        
        if len(mail_name) < 2 or len(domain) < 3 or len(tld) < 2:
            raise ValidationError('Invalid email format')
        
class UsernameValidator:

    def __init__(self):
        pass
    
    def __call__(self, value):
        for char in value:
            if char not in ALLOWED_USERNAME_CHARACTERS:
                raise ValidationError('Username can contain only letters/digits/._-')
        
        if len(value) < 3:
            raise ValidationError('Username must be at least 3 characters long')

class PasswordValidator:

    def __init__(self):
        pass

    def __call__(self, value):
        if len(value) < 8:
            raise ValidationError('Password must be at least 8 characters long')
        elif not any(char.isdigit() for char in value):
            raise ValidationError('Password must contain at least one digit')
        elif not any(char.isupper() for char in value):
            raise ValidationError('Password must contain at least one uppercase letter')
        elif not any(char.islower() for char in value):
            raise ValidationError('Password must contain at least one lowercase letter')

        
