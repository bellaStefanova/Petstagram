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

for acc in Account.objects.all():
    print(acc.__dict__)