# Generated by Django 5.1.3 on 2024-11-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_membership_cardio_membership_functional_training_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='months',
            field=models.CharField(choices=[('one month', 'one'), ('three month', 'Three'), ('six month', 'six'), ('twelve month', 'twelve')], default='Twelve', max_length=12),
        ),
    ]
