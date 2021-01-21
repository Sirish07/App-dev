# Generated by Django 3.1.5 on 2021-01-13 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210113_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Advisors',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='Duration',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='Location',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
