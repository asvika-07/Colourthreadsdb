# Generated by Django 3.2.9 on 2021-11-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminCT', '0024_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cid', models.IntegerField()),
                ('sid', models.IntegerField()),
            ],
            options={
                'db_table': 'Orders',
            },
        ),
    ]
