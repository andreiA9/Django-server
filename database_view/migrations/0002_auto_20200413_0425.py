# Generated by Django 3.1.dev20200402105753 on 2020-04-13 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_view', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='description',
        ),
        migrations.AddField(
            model_name='company',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(default='2020-01-01', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='programmer',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
