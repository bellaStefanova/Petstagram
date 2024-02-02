import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "petstagram.settings")
django.setup()
from petstagram.accounts.models import Account

accounts=Account.objects.all()
for account in accounts:
    print(account.email)
