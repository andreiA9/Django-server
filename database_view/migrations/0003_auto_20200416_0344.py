# Generated by Django 3.1.dev20200402105753 on 2020-04-16 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_view', '0002_auto_20200413_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]