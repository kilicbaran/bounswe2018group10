# Generated by Django 2.1.2 on 2018-10-20 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='user_id',
        ),
    ]
