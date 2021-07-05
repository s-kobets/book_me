# Generated by Django 3.2.4 on 2021-07-02 21:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0006_auto_20210702_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='promoter',
        ),
        migrations.AddField(
            model_name='event',
            name='promoter',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
