# Generated by Django 3.2.9 on 2021-11-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminCT', '0022_remove_stocks_simage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cid', models.IntegerField()),
                ('sid', models.IntegerField()),
            ],
            options={
                'db_table': 'Wishlist',
            },
        ),
    ]