# Generated by Django 4.1 on 2023-01-09 07:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_alter_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='user_following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='user_followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
