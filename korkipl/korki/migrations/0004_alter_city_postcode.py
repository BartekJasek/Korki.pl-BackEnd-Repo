# Generated by Django 4.0.2 on 2023-04-03 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korki', '0003_alter_city_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='postcode',
            field=models.CharField(max_length=7),
        ),
    ]