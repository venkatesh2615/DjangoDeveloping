# Generated by Django 2.2.10 on 2021-02-06 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_changes',
            name='cell',
            field=models.CharField(default='', max_length=32),
        ),
    ]
