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

accounts=Account.objects.all()
for account in accounts:
    print(account.email, account.password)

print(make_password('Test1234'))

email = "abv@abv.bg"
password = "Test1234"

# Authenticate the user
user = authenticate(email=email, password=password)
print(user)

user = Account.objects.get(email="abv@abv.bg")
entered_password = "Test1234"

# Check if the entered password matches the stored password hash
password_matches = check_password(entered_password, user.password)

print(password_matches)

