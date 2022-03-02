# Generated by Django 3.2.9 on 2021-11-18 14:08

import adminCT.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminCT', '0010_adminct_last_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=255)),
                ('scategory', models.CharField(max_length=255)),
                ('simage', models.ImageField(default=adminCT.models.get_default_stock_image, upload_to=adminCT.models.get_stock_image_filepath)),
                ('sqty', models.CharField(max_length=255)),
                ('sprice', models.FloatField()),
                ('sdescription', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='cust_Login',
        ),
    ]
