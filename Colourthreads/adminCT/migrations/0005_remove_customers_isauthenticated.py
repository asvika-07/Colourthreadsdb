# Generated by Django 3.2.9 on 2021-11-17 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminCT', '0004_alter_customers_isauthenticated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='isAuthenticated',
        ),
    ]
