# Generated by Django 3.2.4 on 2021-06-24 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_alter_image_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='ratings',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
