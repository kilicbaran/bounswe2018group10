# Generated by Django 2.1.2 on 2018-11-25 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
