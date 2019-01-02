# Generated by Django 2.1.2 on 2019-01-01 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_semanticsearch'),
        ('user', '0010_auto_20181125_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Tag'),
        ),
        migrations.AddField(
            model_name='freelancerprofile',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Tag'),
        ),
    ]
