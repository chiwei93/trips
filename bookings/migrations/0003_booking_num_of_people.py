# Generated by Django 3.2.4 on 2021-06-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20210625_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='num_of_people',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]