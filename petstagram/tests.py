import os
import django
from django.contrib.auth.hashers import (
    check_password,
    is_password_usable,
    make_password,
    
)
from django.contrib.auth import authenticate



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "petstagram.settings")
django.setup()
from petstagram.accounts.models import Account
from petstagram.pets.models import Pet

# accounts=Account.objects.all()
# for account in accounts:
#     print(account.email, account.password)

# print(make_password('Test1234'))

# email = "abv@abv.bg"
# password = "Test1234"

# Authenticate the user
# user = authenticate(email=email, password=set_password(password))
# print(user)

# user = Account.objects.get(email="bellastefanova7@gmail.com")
# user.
# email=user.email

# password_matches = check_password(password, user.password)
# password=user.password
# if password_matches:
#     # print(email, password)
#     user=authenticate(request=None, email=email, password=password)
# print(user)
# password=user.set_password("Test1234")
# print(password)
# user=authenticate(email=email, password=password)
# print(user)
# entered_password = "Test1234"

# Check if the entered password matches the stored password hash
# password_matches = check_password(entered_password, user.password)

# print(password_matches)

# account=Account()
# account.objects.create_user(username='Bella',first_name='Bella',last_name='Stefanova',password='Test1234', email='some_enail@email.com')

# print(dict(Account.objects.all().values()))
# account=Account.objects.first()
# print(account.password)

# Account.objects.all().delete()
# for acc in Account.objects.all().delete():
#     print(acc.__dict__)

# print([x['username'] for x in Account.objects.all().values('username')])
from petstagram.common.models import ProfilePhotos

for user in Account.objects.all():
    if 'john' in user.username.lower() or 'john' in user.first_name.lower() or 'john' in user.last_name.lower():
        user.profile_picture = '/static/images/add-profile-picture.jpg'
        user.save()
    print(user.__dict__)
    # print(model.user.__dict__)

# for pet in Pet.objects.all():
#     print(pet.name)

# Pet.objects.all().delete()