# Generated by Django 4.1.2 on 2022-10-07 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_rename_image_customers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='socialMedia',
            field=models.CharField(max_length=200),
        ),
    ]
