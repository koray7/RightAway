# Generated by Django 4.0.3 on 2022-03-13 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_grocerylist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocerylist',
            name='category',
        ),
        migrations.RemoveField(
            model_name='grocerylist',
            name='organic',
        ),
    ]