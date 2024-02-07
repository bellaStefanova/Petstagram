# Generated by Django 4.2.4 on 2024-02-07 08:09

from django.db import migrations, models
import petstagram.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', petstagram.accounts.models.AccountManager()),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='profile_picture',
            field=models.URLField(blank=True),
        ),
    ]