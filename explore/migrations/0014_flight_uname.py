# Generated by Django 2.2.20 on 2021-05-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0013_flight_ticketid'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='uname',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
