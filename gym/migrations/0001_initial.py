# Generated by Django 5.1.3 on 2024-11-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('product_code', models.CharField(default=True, max_length=100)),
                ('price', models.FloatField(default=0)),
                ('gst', models.IntegerField(default=0)),
            ],
        ),
    ]
