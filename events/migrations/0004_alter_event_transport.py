# Generated by Django 3.2.4 on 2021-07-02 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_promoter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='transport',
            field=models.ManyToManyField(to='events.Transport'),
        ),
    ]